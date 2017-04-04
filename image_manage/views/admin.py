from flask import Blueprint, render_template, session, redirect, url_for, request, g
from image_manage.database import db

mod = Blueprint('admin', __name__)

@mod.route('/')
def index():
    return render_template('admin/public.html')

@mod.route('/user/list')
def userList():
    return render_template('admin/user/list.html')
