# -*- coding: utf-8 -*-
from datetime import datetime
from flask import Blueprint, render_template, session, redirect, url_for, request, g
from image_manage.databases.database import db
from image_manage.databases.Amodels import  Img, Os, Library, Application, Platform, User
import copy

mod = Blueprint('general', __name__, url_prefix='/general')

@mod.route('/')
def index():
    return render_template('general/index.html')

@mod.route('/list', methods=['GET', 'POST'])
def list():
    pf = db.session.query(Platform).all()
    lib = db.session.query(Library).all()
    app = db.session.query(Application).all()
    os = db.session.query(Os).all()
    m = db.session.query(Img).all()
    messages = copy.deepcopy(m)
    for i in range(0, len(messages)):
        if messages[i].PlatformID !='None':
            for p in pf:
                if p.ID == messages[i].PlatformID:
                    messages[i].PlatformID = p.Name + p.Version

        if messages[i].LibraryID !='None':
            for li in lib:
                if li.ID == messages[i].LibraryID:
                    messages[i].LibraryID = li.Name + li.Version

        if messages[i].AppID !='None':
            for a in app:
                if a.ID == messages[i].AppID:
                    messages[i].AppID = a.Name + a.Version

        if messages[i].OSID !='None':
            for o in os:
                if o.ID == messages[i].OSID:
                    messages[i].OSID = o.Name + o.Version

    return render_template('general/list.html', messages=messages)

@mod.route('/create', methods=['GET', 'POST'])
def create():

    os = []
    messages = db.session.query(Os.Name.distinct().label('Name')).all()
    for m in messages:
        os.append(db.session.query(Os).filter_by(Name=m.Name).all())

    library = []
    messages = db.session.query(Library.Name.distinct().label('Name')).all()
    for m in messages:
        library.append(db.session.query(Library).filter_by(Name=m.Name).all())

    application = []
    messages = db.session.query(Application.Name.distinct().label('Name')).all()
    for m in messages:
        application.append(db.session.query(Application).filter_by(Name=m.Name).all())

    platform = []
    messages = db.session.query(Platform.Name.distinct().label('Name')).all()
    for m in messages:
        platform.append(db.session.query(Platform).filter_by(Name=m.Name).all())

    if request.method == 'POST':
        UUID = 'uuid'
        UserID = 'root'
        ImageName = request.form['ImageName']

        pf_name = request.form.get('pf')
        pf_version = None
        if not pf_name or pf_name == 'None':
            PlatformID = None
        else :
            pf_version = request.form['pf-{}'.format(pf_name)]
            PlatformID = db.session.query(Platform).filter(pf_version == (Platform.Name + Platform.Version)).first().ID

        os_name = request.form['os']
        os_version = request.form['os-{}'.format(os_name)]
        OSID = db.session.query(Os).filter(os_version == (Os.Name + Os.Version)).first().ID

        lib_name = request.form.get('lib', None)
        lib_version = None
        if not lib_name or lib_name == 'None':
            LibraryID = None
        else:
            lib_version = request.form['lib-{}'.format(lib_name)]
            LibraryID = db.session.query(Library).filter(lib_version == (Library.Name + Library.Version)).first().ID

        app_names = request.form.getlist('application')
        app_version = None
        if not app_names or app_names == 'None':
            AppID = None
        else:
            app_name = []
            for n in app_names:
                app_name.append(n)
            app_version = request.form['app-{}'.format(app_name[0])]
            AppID = db.session.query(Application).filter(app_version == (Application.Name + Application.Version)).first().ID

        Description = request.form['Description']
        Public = bool(request.form['Public'])
        Status = 'creating'
        Size = '---'
        UpdateTime = datetime.utcnow()
        Liked = True

        error = [UUID, UserID, ImageName, PlatformID, OSID, LibraryID, AppID, Description, Public, Status, Size, UpdateTime, Liked]

        img = Img(UUID, UserID, ImageName, PlatformID, OSID, LibraryID, AppID, Description, Public, Status, Size, UpdateTime, Liked)
        db.session.add(img)
        db.session.commit()
        return redirect(url_for('general.list'))
    return render_template('general/create.html', platform=platform, os=os, library=library,
                               application=application)


@mod.route('/delete', methods=['GET', 'POST'])
def delete():
    pf = db.session.query(Platform).all()
    lib = db.session.query(Library).all()
    app = db.session.query(Application).all()
    os = db.session.query(Os).all()
    m = db.session.query(Img).all()
    messages = copy.deepcopy(m)
    for i in range(0, len(messages)):
        if messages[i].PlatformID !='None':
            for p in pf:
                if p.ID == messages[i].PlatformID:
                    messages[i].PlatformID = p.Name + p.Version

        if messages[i].LibraryID !='None':
            for li in lib:
                if li.ID == messages[i].LibraryID:
                    messages[i].LibraryID = li.Name + li.Version

        if messages[i].AppID !='None':
            for a in app:
                if a.ID == messages[i].AppID:
                    messages[i].AppID = a.Name + a.Version

        if messages[i].OSID !='None':
            for o in os:
                if o.ID == messages[i].OSID:
                    messages[i].OSID = o.Name + o.Version

    if request.method == 'POST':
        id = request.form.getlist('ID')
        for i in id:
            img = db.session.query(Img).filter_by(ID=i).first()
            db.session.delete(img)
            db.session.commit()
        return redirect(url_for('general.list'))

    return render_template('general/delete.html', messages=messages)

@mod.route('/upload', methods=['GET', 'POST'])
def upload():
    pf = db.session.query(Platform).all()
    lib = db.session.query(Library).all()
    app = db.session.query(Application).all()
    os = db.session.query(Os).all()
    m = db.session.query(Img).all()
    messages = copy.deepcopy(m)
    for i in range(0, len(messages)):
        if messages[i].PlatformID !='None':
            for p in pf:
                if p.ID == messages[i].PlatformID:
                    messages[i].PlatformID = p.Name + p.Version

        if messages[i].LibraryID !='None':
            for li in lib:
                if li.ID == messages[i].LibraryID:
                    messages[i].LibraryID = li.Name + li.Version

        if messages[i].AppID !='None':
            for a in app:
                if a.ID == messages[i].AppID:
                    messages[i].AppID = a.Name + a.Version

        if messages[i].OSID !='None':
            for o in os:
                if o.ID == messages[i].OSID:
                    messages[i].OSID = o.Name + o.Version

    if request.method == 'POST':
        id = request.form.getlist('ID')
        for i in id:
            img = db.session.query(Img).filter_by(ID_id=i).first()

    return render_template('general/upload.html', messages=messages)
