from flask import Blueprint, render_template, session, redirect, url_for, request, g
from image_manage.database import db, Img, User, Platform, Os, Library, Application

mod = Blueprint('image', __name__, url_prefix='/admin/image')
item = ['img_id', 'img_name', 'img_type', 'img_state', 'img_size', 'img_time', 'usr_name']
@mod.route('/')
@mod.route('/list')
def list():
    messages = db.session.query(Img).join(User, Img.img_owner == User.usr_id) \
        .add_columns(Img.img_id, Img.img_name, Img.img_type, Img.img_state, Img.img_size, Img.img_time, User.usr_name,
                     User.usr_id).all()
    return render_template('admin/image/list.html', messages=messages)

@mod.route('/create')
def create():
    os = Os.query.all()
    lib = Library.query.all()
    app = Application.query.all()
    pf = Platform.query.all()
    return render_template('admin/image/create.html', pf=pf, os=os, lib=lib, app=app)

@mod.route('/delete')
def delete():
    messages = db.session.query(Img).join(User, Img.img_owner == User.usr_id) \
        .add_columns(Img.img_id, Img.img_name, Img.img_type, Img.img_state, Img.img_size, Img.img_time, User.usr_name,
                     User.usr_id).all()
    if request.method == 'POST':
        id = request.form.getlist('img_id')
        for i in id:
            img = db.session.query(Img).filter_by(img_id=i).first()
            db.session.delete(img)
            db.session.commit()
        return render_template('admin/image/list.html')
    return render_template('admin/image/delete.html', messages=messages)

@mod.route('/uplaod')
def upload():
    messages = db.session.query(Img).join(User, Img.img_owner == User.usr_id) \
        .add_columns(Img.img_id, Img.img_name, Img.img_type, Img.img_state, Img.img_size, Img.img_time, User.usr_name,
                     User.usr_id).all()
    if request.method == 'POST':
        id = request.form.getlist('img_id')
        for i in id:
            img = db.session.query(Img).filter_by(img_id=i).first()

        return render_template('admin/image/list.html')
    return render_template('admin/image/upload.html', messages=messages)
