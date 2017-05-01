# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, session, redirect, url_for, request, g
from image_manage.databases.database import db
from image_manage.databases.Amodels import  User

mod = Blueprint('user', __name__, url_prefix='/admin/user')
item = [ 'Name', 'Password']
@mod.route('/')
@mod.route('/list')
def list():
    messages = db.session.query(User).all()
    return render_template('admin/user/list.html', messages = messages)

@mod.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        user = db.session.query(User).filter_by(Name=request.form['Name']).first()
        if user == None:
            user = User(request.form['Name'], request.form['Password'])
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('user.list'))
        else:
            error = 'the user name already exits'
            return render_template('admin/user/create.html', item=item, error=error)

    return render_template('admin/user/create.html', item = item)

@mod.route('/delete', methods=['GET', 'POST'])
def delete():
    messages = db.session.query(User).all()
    if request.method == 'POST':
        id = request.form.getlist('ID')
        if not id:
            error = 'no one checked'
            return render_template('admin/user/delete.html', messages=messages, error=error)

        for i in id:
            user = db.session.query(User).filter_by(ID=i).first()
            db.session.delete(user)
            db.session.commit()
        return redirect(url_for('user.list'))

    return render_template('admin/user/delete.html', messages = messages)

@mod.route('/update', methods=['GET', 'POST'])
def update():
    message = {'usr_name' :  'test', 'usr_pwd' : '123', 'usr_group' : 'admin'}
    return render_template('admin/user/update.html', message = message)
