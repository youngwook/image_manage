# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, session, redirect, url_for, request, g
from image_manage.databases.database import db
from image_manage.databases.Amodels import Platform

mod = Blueprint('platform', __name__, url_prefix='/admin/platform')

@mod.route('/')
@mod.route('/list')
def list():
    messages = db.session.query(Platform).all()
    return render_template('admin/platform/list.html', messages=messages)

@mod.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        platform = db.session.query(Platform).filter_by(Name=request.form['Name'], Version=request.form['Version']).first()
        if platform == None:
            platform = Platform(request.form['Name'],request.form['Version'])
            db.session.add(platform)
            db.session.commit()
            return redirect(url_for('platform.list'))
        else:
            error = 'the platform already exits'
            return render_template('admin/platform/create.html', error=error)
    return render_template('admin/platform/create.html')

@mod.route('/delete', methods=['GET', 'POST'])
def delete():
    messages = db.session.query(Platform).all()
    if request.method == 'POST':
        id = request.form.getlist('ID')
        if not id:
            error = 'no one checked'
            return render_template('admin/platform/delete.html', messages=messages, error=error)

        for i in id:
            platform = db.session.query(Platform).filter_by(ID=i).first()
            db.session.delete(platform)
            db.session.commit()
        return redirect(url_for('platform.list'))
    return render_template('admin/platform/delete.html', messages=messages)

'''
@mod.route('/update', methods=['GET', 'POST'])
def update():
    messages = db.session.query(Platform).all()
    if request.method == 'POST':
        for i in messages:
            if i.pf_name != request.form[i.pf_name]:
                p = db.session.query(Platform).filter_by(pf_name=request.form[i.pf_name]).first()
                if p != None:
                    error = 'the platform already exits'
                    return render_template('admin/platform/update.html', messages=messages, error=error)
                platform = db.session.query(Platform).filter_by(pf_name=i.pf_name).first()
                platform.pf_name = request.form[i.pf_name]
                db.session.commit()
        return redirect(url_for('platform.list'))
    return render_template('admin/platform/update.html', messages=messages)
'''