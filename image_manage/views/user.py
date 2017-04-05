from flask import Blueprint, render_template, session, redirect, url_for, request, g
from image_manage.database import db

mod = Blueprint('user', __name__, url_prefix='/admin/user')

@mod.route('/')
@mod.route('/list')
def list():
    messages = [{'usr_name': 'test', 'usr_pwd': '123', 'usr_group': 'admin'},
                {'usr_name': 'test1', 'usr_pwd': '123', 'usr_group': 'general'}
                ]
    return render_template('admin/user/list.html', messages = messages)

@mod.route('/create', methods=['GET', 'POST'])
def create():
    return render_template('admin/user/create.html')

@mod.route('/delete', methods=['GET', 'POST'])
def delete():
    messages = [{'usr_name': 'test', 'usr_pwd': '123', 'usr_group': 'admin'},
                {'usr_name': 'test1', 'usr_pwd': '123', 'usr_group': 'general'}
                ]
    return render_template('admin/user/delete.html', messages = messages)

@mod.route('/update', methods=['GET', 'POST'])
def update():
    message = {'usr_name' :  'test', 'usr_pwd' : '123', 'usr_group' : 'admin'}
    return render_template('admin/user/update.html', message = message)
