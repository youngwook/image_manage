from flask import Blueprint, render_template, session, redirect, url_for, request, g
from image_manage.database import db

mod = Blueprint('image', __name__, url_prefix='/admin/image')

@mod.route('/')
@mod.route('/list')
def list():
    return render_template('admin/image/list.html')

@mod.route('/create')
def create():
    return render_template('admin/image/create.html')

@mod.route('/delete')
def delete():
    return render_template('admin/image/delete.html')

@mod.route('/update')
def update():
    return render_template('admin/image/update.html')
