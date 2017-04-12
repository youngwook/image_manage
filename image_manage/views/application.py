from flask import Blueprint, render_template, session, redirect, url_for, request, g
from image_manage.database import db, Application

mod = Blueprint('application', __name__, url_prefix='/admin/application')
item = [ 'app_name', 'app_group']
@mod.route('/')
@mod.route('/list')
def list():
    messages = db.session.query(Application).all()
    return render_template('admin/application/list.html', messages=messages)

@mod.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        app = db.session.query(Application).filter_by(app_name=request.form['app_name'], app_group=request.form['app_group']).first()
        if app == None:
            app = Application(request.form['app_name'],request.form['app_group'])
            db.session.add(app)
            db.session.commit()
            return redirect(url_for('application.list'))
        else:
            error = 'the application already exits'
            return render_template('admin/application/create.html', error=error, item=item)
    return render_template('admin/application/create.html', item=item)

@mod.route('/delete', methods=['GET', 'POST'])
def delete():
    messages = db.session.query(Application).all()
    if request.method == 'POST':
        id = request.form.getlist('app_id')
        if not id:
            error = 'no one checked'
            return render_template('admin/application/delete.html', messages=messages, error=error)

        for i in id:
            app = db.session.query(Application).filter_by(app_id=i).first()
            db.session.delete(app)
            db.session.commit()
        return redirect(url_for('application.list'))
    return render_template('admin/application/delete.html', messages=messages)

@mod.route('/update', methods=['GET', 'POST'])
def update():
    messages = db.session.query(Application).all()
    if request.method == 'POST':
        for i in messages:
            if i.app_name != request.form[i.app_name+str(i.app_id)]:
                apps = db.session.query(Application).filter_by(app_group=request.form[str(i.app_id)+i.app_group]).all()
                for o in apps:
                    if o.app_name == request.form[i.app_name+str(i.app_id)]:
                        error = 'the type have this version'
                        return render_template('admin/application/update.html', messages=messages, error=error)
                app = db.session.query(Application).filter_by(app_name=i.app_name, app_group=i.app_group).first()
                app.app_name = request.form[i.app_name+str(i.app_id)]
                db.session.commit()

            if i.app_group != request.form[str(i.app_id)+i.app_group]:
                apps = db.session.query(Application).filter_by(app_group=request.form[str(i.app_id)+i.app_group]).all()
                for o in apps:
                    if o.app_name == i.app_name:
                        error = 'the type have this version'
                        return render_template('admin/application/update.html', messages=messages, error=error)
                app = db.session.query(Application).filter_by(app_name=i.app_name, app_group=i.app_group).first()
                app.app_group = request.form[str(i.app_id)+i.app_group]
                db.session.commit()
        return redirect(url_for('application.list'))
    return render_template('admin/application/update.html', messages=messages)
