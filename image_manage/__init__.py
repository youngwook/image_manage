import time
from sqlite3 import dbapi2 as sqlite3
from datetime import datetime, timedelta
from flask import Flask,render_template, request, session, url_for, redirect, g
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.permanent_session_lifetime = timedelta(seconds=30)
app.config.from_object('config')

from database import  User, Img, db

def format_datetime(date):
    '''format a times for display'''
    return datetime.utcfromtimestamp(date).strftime('%Y.%m.%d %H:%M')

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


@app.route('/')
def public():

    return render_template('index.html')

@app.route('/create', methods=['GET', 'POST'])
def create():
    if g.user == None:
        return redirect(url_for('public'))
    if request.method == 'POST':
        type = request.form['type']
        os = request.form['os-centos']
        os = os + ', '+request.form['os-ubuntu']
        os = os + ', '+request.form['os-fedora']
        lib = request.form['lib-openmpi']
        lib = lib + ', '+request.form['lib-mpich']
        ssh = request.form['ssh']
        img_name = request.form['img_name']
        message = 'type is {0}, os is {1}, lib is {2}, ssh is {3}, img_name is {4},'.format(type, os, lib, ssh, img_name)
        return render_template('index.html', message= message)
    return render_template('create.html')

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if g.user == None:
        return redirect(url_for('public'))
    if request.method == 'POST':
        id = request.form.getlist('id')
        message = ''
        for i in id:
            message = message + i
            img = db.session.query(Img).filter_by(img_id=i).first()
            db.session.delete(img)
            db.session.commit()
        return render_template('index.html', message=message)

    messages = db.session.query(Img).join(User,  Img.owner==User.usr_id)\
        .add_columns(Img.img_id, Img.img_name, Img.type, Img.state, Img.size, Img.time, User.usr_name, User.usr_id).all()
    return render_template('delete.html', messages = messages)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if g.user == None:
        return redirect(url_for('public'))
    if request.method == 'POST':
        id = request.form.getlist('id')
        if id == None:
            message = None
        else:
            message = 'the selecte id is {0} size is {1}'.format(id[0], len(id))
        return render_template('index.html', message=message)

    messages = db.session.query(Img).join(User,  Img.owner==User.usr_id)\
        .add_columns(Img.img_id, Img.img_name, Img.type, Img.state, Img.size, Img.time, User.usr_name, User.usr_id).all()
    return render_template('update.html', messages = messages)

@app.route('/login', methods=['GET','POST'])
def login():
    if g.user:
        return redirect(url_for('public'))
    error = None

    if request.method == 'POST':

        user = db.session.query(User).filter_by(usr_name=request.form['usr_name']).first()
        if user is None:
            error = 'Invalid username'
        elif user.pwd != request.form['pwd']:
            error = 'Invalid password'
        else:
            session['usr_id'] = user.usr_id
            return redirect(url_for('list'))
    return render_template('login.html', error = error)

@app.route('/list')
def list():
    if g.user == None:
        return redirect(url_for('public'))
    messages = db.session.query(Img).join(User,  Img.owner==User.usr_id)\
        .add_columns(Img.img_id, Img.img_name, Img.type, Img.state, Img.size, Img.time, User.usr_name, User.usr_id).all()
    return render_template('list.html', messages = messages)

app.jinja_env.filters['timeformat'] = format_datetime

