import time
from sqlite3 import dbapi2 as sqlite3
from datetime import datetime, timedelta
from flask import Flask,render_template, request, session, url_for, redirect, g
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
app.permanent_session_lifetime = timedelta(seconds=30)
from image_manage.database import db, User

@app.before_request
def before_request():
    '''make sure we are connected to the db each request and look up the current user so that we know he is there'''

    g.user = None
    if 'usr_id' in session:
        g.user = db.session.query(User).filter_by(usr_id=session['usr_id']).first()

@app.teardown_request
def teardown_request(exception):
    '''closes the db at each of end of request'''
    db.session.remove()

from image_manage.views import login
from image_manage.views import admin
from image_manage.views import general
from image_manage.views import user
from image_manage.views import platform
from image_manage.views import os
from image_manage.views import library
from image_manage.views import application
from image_manage.views import image

app.register_blueprint(login.mod)
app.register_blueprint(admin.mod)
app.register_blueprint(general.mod)
app.register_blueprint(user.mod)
app.register_blueprint(platform.mod)
app.register_blueprint(os.mod)
app.register_blueprint(library.mod)
app.register_blueprint(application.mod)
app.register_blueprint(image.mod)

