
from flask_sqlalchemy import SQLAlchemy
from image_manage import app

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__='user'
    usr_id = db.Column('usr_id', db.Integer, primary_key=True)
    usr_name = db.Column('usr_name', db.String(100))
    usr_pwd = db.Column('usr_pwd', db.String(100))
    usr_group = db.Column('usr_group', db.String(100))

    def __init__(self, usr_name, usr_pwd, usr_group):
        self.usr_name = usr_name
        self.usr_pwd = usr_pwd
        self.usr_group = usr_group




class Img(db.Model):
    __tablename__ = 'img'
    img_id = db.Column('img_id', db.Integer, primary_key=True)
    img_name = db.Column('img_name', db.String(100))
    img_type = db.Column('img_type', db.String(100))
    img_state = db.Column('img_state', db.String(100))
    img_size = db.Column('img_size', db.String(100))
    img_time = db.Column('img_time', db.DateTime)
    img_owner = db.Column('img_owner', db.Integer)

    def __init__(self, name, type, state, size, time, owner):
        self.img_name = name
        self.img_type = type
        self.img_state = state
        self.img_size = size
        self.img_time = time
        self.img_owner = owner


class Platform(db.Model):
    __tablename__ = 'platform'

    pf_id = db.Column('pf_id', db.Integer, primary_key = True)
    pf_name = db.Column('pf_name', db.String(100))

    def __init__(self, pf_name):
        self.pf_name = pf_name

class Library(db.Model):
    __tablename__ = 'library'

    lib_id = db.Column('lib_id', db.Integer, primary_key = True)
    lib_type = db.Column('lib_type', db.String(100))
    lib_version = db.Column('lib_version', db.String(100))

    def __init__(self, lib_type, lib_version):
        self.lib_type = lib_type
        self.lib_version = lib_version

class Os(db.Model):
    __tablename__ = 'os'

    os_id = db.Column('os_id', db.Integer, primary_key = True)
    os_type = db.Column('os_type', db.String(100))
    os_version = db.Column('os_version', db.String(100))

    def __init__(self, os_type, os_version):
        self.os_type = os_type
        self.os_version = os_version

class Application(db.Model):
    __tablename__ = 'application'

    app_id = db.Column('app_id', db.Integer, primary_key = True)
    app_name = db.Column('app_name', db.String(100))
    app_group = db.Column('app_group', db.String(100))

    def __init__(self, app_name, app_group):
        self.app_name = app_name
        self.app_group = app_group

def init_db():
    db.create_all()
    print 'db success!'

