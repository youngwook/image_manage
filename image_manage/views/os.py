# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, session, redirect, url_for, request, g
from image_manage.databases.database import db
from image_manage.databases.Amodels import  Os
from image_manage.views.admin import check

mod = Blueprint('os', __name__, url_prefix='/admin/os')
item = [ 'Name', 'Version']
@mod.route('/')
@mod.route('/list')
def list():
    check()
    messages = db.session.query(Os).all()
    return render_template('admin/os/list.html', messages=messages)

@mod.route('/create', methods=['GET', 'POST'])
def create():
    check()
    if request.method == 'POST':
        os = db.session.query(Os).filter_by(Name=request.form['Name'], Version=request.form['Version']).first()
        if os == None:
            os = Os(request.form['Name'],request.form['Version'])
            db.session.add(os)
            db.session.commit()
            return redirect(url_for('os.list'))
        else:
            error = 'the os already exits'
            return render_template('admin/os/create.html', error=error, item=item)
    return render_template('admin/os/create.html', item=item)

@mod.route('/delete', methods=['GET', 'POST'])
def delete():
    check()
    messages = db.session.query(Os).all()
    if request.method == 'POST':
        id = request.form.getlist('ID')
        if not id:
            error = 'no one checked'
            return render_template('admin/os/delete.html', messages=messages, error=error)

        for i in id:
            os = db.session.query(Os).filter_by(ID=i).first()
            db.session.delete(os)
            db.session.commit()
        return redirect(url_for('os.list'))
    return render_template('admin/os/delete.html', messages=messages)

'''
@mod.route('/update', methods=['GET', 'POST'])
def update():
    messages = db.session.query(Os).all()
    if request.method == 'POST':
        for i in messages:
            if i.os_type != request.form[i.os_type+str(i.os_id)]:
                oss = db.session.query(Os).filter_by(os_type=request.form[i.os_type+str(i.os_id)]).all()
                for o in oss:
                    if o.os_version == i.os_version:
                        error = 'the type have this version'
                        return render_template('admin/os/update.html', messages=messages, error=error)
                os = db.session.query(Os).filter_by(os_type=i.os_type, os_version=i.os_version).first()
                os.os_type = request.form[i.os_type+str(i.os_id)]
                db.session.commit()

            if i.os_version != request.form[str(i.os_id)+i.os_version]:
                oss = db.session.query(Os).filter_by(os_type=request.form[i.os_type+str(i.os_id)]).all()
                for o in oss:
                    if o.os_version == request.form[str(i.os_id)+i.os_version]:
                        error = 'the type have this version'
                        return render_template('admin/os/update.html', messages=messages, error=error)
                os = db.session.query(Os).filter_by(os_type=i.os_type, os_version=i.os_version).first()
                os.os_version = request.form[str(i.os_id)+i.os_version]
                db.session.commit()
        return redirect(url_for('os.list'))
    return render_template('admin/os/update.html', messages=messages)
'''