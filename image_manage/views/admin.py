# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, session, redirect, url_for, request, g
from image_manage import sshConnector
from image_manage.databases.database import db
from image_manage.databases.Amodels import  Img, Os, Library, Application, Platform, User

mod = Blueprint('admin', __name__, url_prefix='/admin')


@mod.route('/')
def index():

    check()

    return render_template('admin/index_admin.html')

@mod.route('/shell/')
def shell():
    if sshConnector.has_key(g.user):
        hi = sshConnector[g.user].command(g.user)
    else :
        hi = "failed"
    return render_template('shell.html', hi = hi)

def check():
    if g.user:
        user = db.session.query(User).filter_by(Name=g.user).first()

        if user:
            pass
        else:
            return redirect(url_for('general.index'))
    else:
        return redirect(url_for('login.index'))