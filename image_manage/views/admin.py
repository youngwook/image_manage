# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, session, redirect, url_for, request, g
from image_manage import sshConnector

mod = Blueprint('admin', __name__, url_prefix='/admin')


@mod.route('/')
def index():
    return render_template('admin/index_admin.html')

@mod.route('/shell/')
def shell():
    if sshConnector.has_key(g.user):
        hi = sshConnector[g.user].command()
    else :
        hi = "failed"
    return render_template('shell.html', hi = hi)
