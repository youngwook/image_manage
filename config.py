import os

'''get current path'''
basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = False

SECRET_KEY = 'HELLO'
#DATABASE_URI = 'sqlite:///'+ os.path.join(basedir, 'img.db')
#SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123@localhost/test'
#SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://webapp:123@117.16.149.113/test'
#SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://webapp:123@117.16.149.113/images'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://webapp:123@117.16.146.98/images'
SQLALCHEMY_TRACK_MODIFICATIONS = True
del os