from flask import Blueprint, render_template, session, redirect, url_for, request, g
from image_manage.database import db

mod = Blueprint('general', __name__, url_prefix='/general')

@mod.route('/')
def index():
    return render_template('general/index.html')

@mod.route('/list')
def userList():
    return render_template('general/list.html')
