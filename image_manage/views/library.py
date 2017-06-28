# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, session, redirect, url_for, request, g
from image_manage.databases.database import db
from image_manage.databases.Amodels import  Library
from image_manage.views.admin import check

mod = Blueprint('library', __name__, url_prefix='/admin/library')
item = [ 'Name', 'Version']

@mod.route('/')
@mod.route('/list')
def list():
    check()
    messages = db.session.query(Library).all()
    return render_template('admin/library/list.html', messages=messages)

@mod.route('/create', methods=['GET', 'POST'])
def create():
    check()
    if request.method == 'POST':
        library = db.session.query(Library).filter_by(Name=request.form['Name'], Version=request.form['Version']).first()
        if library == None:
            library = Library(request.form['Name'],request.form['Version'])
            db.session.add(library)
            db.session.commit()
            return redirect(url_for('library.list'))
        else:
            error = 'the library already exits'
            return render_template('admin/library/create.html', error=error, item=item)
    return render_template('admin/library/create.html', item=item)

@mod.route('/delete', methods=['GET', 'POST'])
def delete():
    check()
    messages = db.session.query(Library).all()
    if request.method == 'POST':
        id = request.form.getlist('ID')
        if not id:
            error = 'no one checked'
            return render_template('admin/library/delete.html', messages=messages, error=error)

        for i in id:
            os = db.session.query(Library).filter_by(ID=i).first()
            db.session.delete(os)
            db.session.commit()
        return redirect(url_for('library.list'))
    return render_template('admin/library/delete.html', messages=messages)

'''
@mod.route('/update', methods=['GET', 'POST'])
def update():
    messages = db.session.query(Library).all()
    if request.method == 'POST':
        for i in messages:
            if i.lib_type != request.form[i.lib_type+str(i.lib_id)]:
                libs = db.session.query(Library).filter_by(lib_type=request.form[i.lib_type+str(i.lib_id)]).all()
                for o in libs:
                    if o.lib_version == i.lib_version:
                        error = 'the type have this version'
                        return render_template('admin/library/update.html', messages=messages, error=error)
                lib = db.session.query(Library).filter_by(lib_type=i.lib_type, lib_version=i.lib_version).first()
                lib.lib_type = request.form[i.lib_type+str(i.lib_id)]
                db.session.commit()

            if i.lib_version != request.form[str(i.lib_id)+i.lib_version]:
                libs = db.session.query(Library).filter_by(lib_type=request.form[i.lib_type+str(i.lib_id)]).all()
                for o in libs:
                    if o.lib_version == request.form[str(i.lib_id)+i.lib_version]:
                        error = 'the type have this version'
                        return render_template('admin/library/update.html', messages=messages, error=error)
                lib = db.session.query(Library).filter_by(lib_type=i.lib_type, lib_version=i.lib_version).first()
                lib.lib_version = request.form[str(i.lib_id)+i.lib_version]
                db.session.commit()
        return redirect(url_for('library.list'))
    return render_template('admin/library/update.html', messages=messages)
'''