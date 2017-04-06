from flask import Blueprint, render_template, session, redirect, url_for, request, g
from image_manage.database import db, User

mod = Blueprint('login', __name__)

@mod.route('/')
def index():
    return render_template('index.html')

@mod.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        user = db.session.query(User).filter_by(usr_name=request.form['usr_name']).first()
        if user is None:
            error = 'Invalid username'
        elif user.usr_pwd != request.form['usr_pwd']:
            error = 'Invalid password'
        else:
            session['usr_id'] = user.usr_id
            if user.usr_group == 'admin':
                return redirect(url_for('admin.index'))
            else:
                return redirect(url_for('general.index'))

    return render_template('login.html', error=error)

@mod.route('/logout')
def logout():
    session.pop('usr_id', None)
    return redirect(url_for('login.index'))
