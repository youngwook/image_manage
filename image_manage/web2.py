
from datetime import datetime, timedelta
from flask import Flask,render_template, request, session, url_for, redirect, g
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

from image_manage.views import login
from image_manage.views import admin
from image_manage.views import general
from image_manage.views import user

app.register_blueprint(login.mod)
app.register_blueprint(admin.mod)
app.register_blueprint(general.mod)
app.register_blueprint(user.mod)

if __name__ == "__main__":
    app.debug = True
    app.run(host="117.16.149.113")