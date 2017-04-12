from flask import Blueprint, render_template, session, redirect, url_for, request, g
from image_manage.database import db, User

mod = Blueprint('login', __name__)

@mod.route('/')
def index():
    return render_template('index.html')

@mod.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        return redirect(url_for('admin.index'))

    return render_template('login.html')

@mod.route('/logout')
def logout():
    return redirect(url_for('login.index'))
