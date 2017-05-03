# -*- coding: utf-8 -*-
from datetime import datetime
from flask import Blueprint, render_template, session, redirect, url_for, request, g
from image_manage.databases.database import db
from image_manage.databases.Amodels import  Img, Os, Library, Application, Platform, User

mod = Blueprint('image', __name__, url_prefix='/admin/image')
item = ['img_id', 'img_name', 'img_type', 'img_state', 'img_size', 'img_time', 'usr_name']

@mod.route('/')
@mod.route('/list')
def list():
    messages = db.session.query(Img.ID, Img.UUID, Img.UserID, Img.ImageName,
                                (Platform.Name + Platform.Version).label('PlatformID'),
                                (Os.Name + Os.Version).label('OSID'),
                                (Library.Name + Library.Version).label('LibraryID'),
                                (Application.Name + Application.Version).label('AppID'),
                                Img.Description, Img.Public, Img.Status, Img.Size, Img.UpdateTime, Img.Liked) \
        .filter(Img.PlatformID == Platform.ID,
                Img.OSID == Os.ID,
                Img.LibraryID == Library.ID,
                Img.AppID == Application.ID).all()
    return render_template('admin/image/list.html', messages=messages)

@mod.route('/create', methods=['GET', 'POST'])
def create():

    os = []
    messages = db.session.query(Os.os_type.distinct().label('os_type')).all()
    for m in messages:
        os.append(db.session.query(Os).filter_by(os_type=m.os_type).all())

    lib = []
    messages = db.session.query(Library.lib_type.distinct().label('lib_type')).all()
    for m in messages:
        lib.append(db.session.query(Library).filter_by(lib_type=m.lib_type).all())

    app = []
    messages = db.session.query(Application.app_group.distinct().label('app_group')).all()
    for m in messages:
        app.append(db.session.query(Application).filter_by(app_group=m.app_group).all())

    pf = Platform.query.all()

    if request.method == 'POST':
        img_name = request.form['img_name']
        img_type = request.form['img_type']
        for o in os:
            os_type = request.form['os']
            if (os_type == o[0].os_type):
                os_version =  request.form['os-{}'.format(os_type)]

        for l in lib:
            lib_type = request.form['lib']
            if (lib_type == l[0].lib_type):
                lib_version =  request.form['lib-{}'.format(lib_type)]

        app_name = []
        for a in app:
            app_groups = request.form.getlist('application')
            for app_group in app_groups:
                if (app_group == a[0].app_group):
                    app_name.append(a)

        img = db.session.query(Img).filter_by(img_name=request.form['img_name']).first()
        if img == None:
            img = Img(img_name,img_type,"creating","---",datetime.utcnow(),2)
            db.session.add(img)
            db.session.commit()
            return redirect(url_for('image.list'))
        else:
            error = 'the user name already exits'
            return render_template('admin/image/create.html', pf=pf, os=os, lib=lib, app=app, error=error)

        message = 'img name is {0}, img_type is {1}, os is {2}, lib is {3}, application is {4},,'.format(img_name, img_type, os_version, lib_version, app_name)
        return render_template('admin/image/create.html', pf=pf, os=os, lib=lib, app=app, message=message)
    return render_template('admin/image/create.html', pf=pf, os=os, lib=lib, app=app)

@mod.route('/delete', methods=['GET', 'POST'])
def delete():
    messages = db.session.query(Img.ID, Img.UUID, Img.UserID, Img.ImageName,
                                (Platform.Name + Platform.Version).label('PlatformID'),
                                (Os.Name + Os.Version).label('OSID'),
                                (Library.Name + Library.Version).label('LibraryID'),
                                (Application.Name + Application.Version).label('AppID'),
                                Img.Description, Img.Public, Img.Status, Img.Size, Img.UpdateTime, Img.Liked) \
        .filter(Img.PlatformID == Platform.ID,
                Img.OSID == Os.ID,
                Img.LibraryID == Library.ID,
                Img.AppID == Application.ID).all()
    if request.method == 'POST':
        id = request.form.getlist('ID')
        for i in id:
            img = db.session.query(Img).filter_by(ID=i).first()
            db.session.delete(img)
            db.session.commit()
            return redirect(url_for('image.list'))
    return render_template('admin/image/delete.html', messages=messages)

@mod.route('/uplaod', methods=['GET', 'POST'])
def upload():
    messages = db.session.query(Img.ID, Img.UUID, Img.UserID, Img.ImageName,
                                (Platform.Name + Platform.Version).label('PlatformID'),
                                (Os.Name + Os.Version).label('OSID'),
                                (Library.Name + Library.Version).label('LibraryID'),
                                (Application.Name + Application.Version).label('AppID'),
                                Img.Description, Img.Public, Img.Status, Img.Size, Img.UpdateTime, Img.Liked) \
        .filter(Img.PlatformID == Platform.ID,
                Img.OSID == Os.ID,
                Img.LibraryID == Library.ID,
                Img.AppID == Application.ID).all()
    if request.method == 'POST':
        id = request.form.getlist('ID')
        for i in id:
            img = db.session.query(Img).filter_by(ID_id=i).first()

            return redirect(url_for('image.list'))
    return render_template('admin/image/upload.html', messages=messages)
