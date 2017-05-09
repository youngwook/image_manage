# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
from flask import Flask,render_template, request, session, url_for, redirect, g

app = Flask(__name__)

from sys import platform as pf

if pf == "linux" or pf == "linux2":
    app.config.from_object('config')
elif pf == "win32":
    app.config.from_object('config_for_windows')

app.permanent_session_lifetime = timedelta(seconds=30)
from image_manage.databases.database import db

@app.before_request
def before_request():
    '''요청이 들어오기 전에 세션 체크 '''
    g.user = None
    if 'user' in session:
        g.user = session['user']
    if g.user == None:
        if hasattr(g, 'ssh'):
            g.ssh.close()
            g.ssh = None

@app.teardown_request
def teardown_request(exception):
    '''요청이 끝날 때 데이터베이스 연결 차단'''

    db.session.remove()

from image_manage.views import login
from image_manage.views import admin
from image_manage.views import user

from image_manage.views import platform
from image_manage.views import os
from image_manage.views import library
from image_manage.views import application
from image_manage.views import image
from image_manage.views import general


app.register_blueprint(login.mod)
app.register_blueprint(admin.mod)
app.register_blueprint(user.mod)

app.register_blueprint(platform.mod)
app.register_blueprint(os.mod)
app.register_blueprint(library.mod)
app.register_blueprint(application.mod)
app.register_blueprint(image.mod)
app.register_blueprint(general.mod)

