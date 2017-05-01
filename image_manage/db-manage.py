import time
from datetime import datetime
from databases.database import db, init_db
from databases.Amodels import User, Platform, Application, Img, Os, Library

print 'getting start with mysql database-images init()'
init_db()

print 'create user'
user = User('root','123')
db.session.add(user)
db.session.commit()

query = User.query.all()
for i in query:
    print(i.Name)



print 'create Platform'

print 'create Application'

print 'create Image'

print 'create OS'

print 'create Library'

db.session.remove()