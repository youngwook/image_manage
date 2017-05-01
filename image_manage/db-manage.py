import time
from datetime import datetime
from databases.database import db, init_db

#init_db()

'''user = User('root','123','admin')
databases.session.add(user)

databases.session.commit()

query = User.query.all()
for i in query:
    print(i.usr_name)

databases.session.remove()
'''


db.session.remove()