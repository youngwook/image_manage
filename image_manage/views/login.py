# -*- coding: utf-8 -*-
from datetime import datetime
from sqlalchemy import desc
from flask import Blueprint, render_template, session, redirect, url_for, request, g
from image_manage.databases.database import db
from image_manage.databases.Amodels import  Img, Os, Library, Application, Platform, User
from image_manage.otp import sshConnect

mod = Blueprint('login', __name__)

@mod.route('/')
def index():
    return render_template('index.html')

@mod.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        account = request.form['account']
        ps = request.form['pwd']
        otp = request.form['otp']

        ssh = sshConnect(account, ps, otp)
        if ssh != None:
            g.user = account.split('@')[0]
            g.ssh = ssh
            user = db.session.query(User).filter_by(Name=g.user).first()
            if g.user == user:
                return redirect(url_for('admin.index'))
            else:
                redirect(url_for('general.index'))

            error = ''
            return render_template('login.html', error = error)

    return render_template('login.html')

@mod.route('/logout')
def logout():
    g.ssh.close()
    g.user = None
    g.ssh = None
    return redirect(url_for('login.index'))
