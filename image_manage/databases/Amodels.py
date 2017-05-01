from flask_sqlalchemy import SQLAlchemy
from image_manage.databases.database import db


class User(db.Model):
    __tablename__='user'
    ID = db.Column('ID', db.Integer, primary_key=True)
    Name = db.Column('Name', db.String(100))
    Password = db.Column('Password', db.String(20))

    def __init__(self, Name, Password):
        self.Name = Name
        self.Password = Password

    def as_dict(self):
        return {x.name: getattr(self, x.name) for x in self.__table__.columns}


class Platform(db.Model):
    __tablename__ = 'platform_tag'

    ID = db.Column('ID', db.Integer, primary_key = True)
    Name = db.Column('Name', db.String(100))
    Version = db.Column('Version', db.String(20))

    def __init__(self, Name, Version):
        self.Name = Name
        self.Version = Version

    def as_dict(self):
        return {x.name: getattr(self, x.name) for x in self.__table__.columns}

class Library(db.Model):
    __tablename__ = 'library_tag'

    ID = db.Column('ID', db.Integer, primary_key = True)
    Name = db.Column('Name', db.String(100))
    Version = db.Column('Version', db.String(20))

    def __init__(self, Name, Version):
        self.Name = Name
        self.Version = Version

    def as_dict(self):
        return {x.name: getattr(self, x.name) for x in self.__table__.columns}

class Os(db.Model):
    __tablename__ = 'os_tag'

    ID = db.Column('ID', db.Integer, primary_key = True)
    Name = db.Column('Name', db.String(100))
    Version = db.Column('Version', db.String(20))

    def __init__(self, Name, Version):
        self.Name = Name
        self.Version = Version

    def as_dict(self):
        return {x.name: getattr(self, x.name) for x in self.__table__.columns}

class Application(db.Model):
    __tablename__ = 'app_tag'

    ID = db.Column('ID', db.Integer, primary_key = True)
    Name = db.Column('Name', db.String(100))
    Version = db.Column('Version', db.String(20))

    def __init__(self, Name, Version):
        self.Name = Name
        self.Version = Version

    def as_dict(self):
        return {x.name: getattr(self, x.name) for x in self.__table__.columns}

class Img(db.Model):
    __tablename__ = 'imgage_meta'

    ID = db.Column('ID', db.Integer, primary_key=True)
    UUID = db.Column('UUID', db.String(100))
    UserID = db.Column('UserID', db.String(20))
    ImageName = db.Column('ImageName', db.String(100))
    PlatformID = db.Column('PlatformID', db.Integer)
    OSID = db.Column('OSID', db.Integer)
    LibraryID = db.Column('LibraryID', db.Integer)
    AppID = db.Column('AppID', db.Integer)
    Description = db.Column('Description', db.String(100))
    Public = db.Column('Public', db.Boolean, default = False, nuallable = False)
    Status = db.Column('Status', db.String(20))
    Size = db.Column('Size', db.String(20))
    UpdateTime = db.Column('UpdateTime', db.DateTime)
    Liked = db.Column('Liked', db.Boolean, default = False, nuallable = True)

    def __init__(self, ID, UUID, UserID, ImageName, PlatformID, OSID, LibraryID, AppID, Description, Public, Status, Size, UpdateTime, Liked):
        self.ID = ID
        self.UUID = UUID
        self.UserID = UserID
        self.ImageName = ImageName
        self.PlatformID = PlatformID
        self.OSID = OSID
        self.LibraryID = LibraryID
        self.AppID = AppID
        self.Description = Description
        self.Public = Public
        self.Status = Status
        self.Size = Size
        self.UpdateTime = UpdateTime
        self.Liked = Liked

    def as_dict(self):
        return {x.name: getattr(self, x.name) for x in self.__table__.columns}