from flask_sqlalchemy import SQLAlchemy
from image_manage import app

db = SQLAlchemy(app)

def init_db():
    import image_manage.databases.models
    db.create_all()
    print 'databases success!'