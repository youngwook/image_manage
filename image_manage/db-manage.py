import time
from datetime import datetime
from database import db, init_db, Img, User, Platform, Os, Library, Application

#init_db()

'''user = User('root','123','admin')
db.session.add(user)

db.session.commit()

query = User.query.all()
for i in query:
    print(i.usr_name)

db.session.remove()
'''
os = []
messages = db.session.query(Os.os_type.distinct().label('os_type')).all()
for m in messages:
    os.append( db.session.query(Os).filter_by(os_type=m.os_type).all())

for oa in os:
    for o in oa:
        print(o.os_type+":"+o.os_version)
    print("-----------------")

db.session.remove()