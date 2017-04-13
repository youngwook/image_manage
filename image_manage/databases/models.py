from flask_sqlalchemy import SQLAlchemy
from image_manage.databases.database import db


class User(db.Model):
    __tablename__='user'
    usr_id = db.Column('usr_id', db.Integer, primary_key=True)
    usr_name = db.Column('usr_name', db.String(100))
    usr_pwd = db.Column('usr_pwd', db.String())

    def __init__(self, usr_name, usr_pwd):
        self.usr_name = usr_name
        self.usr_pwd = usr_pwd

    def as_dict(self):
        return {x.name: getattr(self, x.name) for x in self.__table__.columns}


class Platform(db.Model):
    __tablename__ = 'plat_tag'

    plat_id = db.Column('plat_id', db.Integer, primary_key = True)
    plat_name = db.Column('plat_name', db.String(100))
    plar_version = db.Column('plat_version', db.String(100))

    def __init__(self, plat_name, plat_version):
        self.plat_name = plat_name
        self.plat_version = plat_version

    def as_dict(self):
        return {x.name: getattr(self, x.name) for x in self.__table__.columns}

class Library(db.Model):
    __tablename__ = 'lib_tag'

    lib_id = db.Column('lib_id', db.Integer, primary_key = True)
    lib_name = db.Column('lib_name', db.String(100))
    lib_version = db.Column('lib_version', db.String(100))

    def __init__(self, lib_name, lib_version):
        self.lib_name = lib_name
        self.lib_version = lib_version

    def as_dict(self):
        return {x.name: getattr(self, x.name) for x in self.__table__.columns}

class Os(db.Model):
    __tablename__ = 'os_tag'

    os_id = db.Column('os_id', db.Integer, primary_key = True)
    os_name = db.Column('os_name', db.String(100))
    os_version = db.Column('os_version', db.String(100))

    def __init__(self, os_name, os_version):
        self.os_name = os_name
        self.os_version = os_version

    def as_dict(self):
        return {x.name: getattr(self, x.name) for x in self.__table__.columns}

class Application(db.Model):
    __tablename__ = 'app_tag'

    app_id = db.Column('app_id', db.Integer, primary_key = True)
    app_name = db.Column('app_name', db.String(100))
    app_version = db.Column('app_version', db.String(100))

    def __init__(self, app_name, app_version):
        self.app_name = app_name
        self.app_version = app_version

    def as_dict(self):
        return {x.name: getattr(self, x.name) for x in self.__table__.columns}

class Img(db.Model):
    __tablename__ = 'img'
    id = db.Column('id', db.Integer, primary_key=True)
    img_id = db.Column('img_id', db.String(100))
    user_id = db.Column('user_id', db.String(100))
    img_plat = db.Column('img_plat', db.Integer)
    img_os = db.Column('img_os', db.Integer)
    img_lib = db.Column('img_lib', db.Integer)
    img_app = db.Column('img_app', db.Integer)
    img_name = db.Column('img_name', db.String(100))
    img_disc = db.Column('img_disc', db.String())
    img_time = db.Column('img_time', db.DateTime)
    img_pub = db.Column('img_pub', db.Boolean)
    img_status = db.Column('img_status', db.String(100))
    img_size = db.Column('img_size', db.String(100))

    def __init__(self, img_id, user_id, img_plat, img_os, img_lib, img_app, img_name, img_disc, img_time, img_pub, img_status, img_size,):
        self.img_id = img_id
        self.user_id = user_id
        self.img_plat = img_plat
        self.img_os = img_os
        self.img_lib = img_lib
        self.img_app = img_app
        self.img_name = img_name
        self.img_disc = img_disc
        self.img_time = img_time
        self.img_pub = img_pub
        self.img_status = img_status
        self.img_size = img_size

    def as_dict(self):
        return {x.name: getattr(self, x.name) for x in self.__table__.columns}