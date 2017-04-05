import time
from datetime import datetime
from database import db, init_db, User, Img, init_db

#init_db()

'''user = User('root','123','admin')
db.session.add(user)

db.session.commit()

query = User.query.all()
for i in query:
    print(i.usr_name)

db.session.remove()
'''
messages = db.session.query(User).all()
for m in messages:
    print(m.usr_name+ m.usr_group)

db.session.remove()