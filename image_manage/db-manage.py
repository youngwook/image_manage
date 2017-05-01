from datetime import datetime
from image_manage.databases.database import db, init_db
from image_manage.databases.Amodels import User, Platform, Application, Img, Os, Library

'''
print 'getting start with mysql database-images init()'
init_db()

'''

'''
print 'create user'
user = User('root','123')
db.session.add(user)
db.session.commit()

query = User.query.all()
for i in query:
    print(i.Name)
'''

'''
print 'create Platform'
plat = Platform('docker','')
plat1 = Platform('singularity','')
db.session.add_all([plat,plat1])
db.session.commit()


print 'create Application'
hpl = Application('hpl','')
db.session.add(hpl)
db.session.commit()

print 'create OS'
os = Os('centos','7')
os1 = Os('centos','6')
os2 = Os('centos','5')
os3 = Os('ubuntu','12')
os4 = Os('centos','14')
os5 = Os('fedora','')
db.session.add_all([os,os1,os2,os3,os4,os5])
db.session.commit()

print 'create Library'
lib = Library('openmpi','2')
lib1 = Library('openmpi','1')
lib2 = Library('mpich','3')
lib3 = Library('mpich','2')
db.session.add_all([lib,lib1,lib2,lib3])
db.session.commit()

print 'create Image'
image = Img('uuid', 'root', 'centos', 1, 1, 1, 1, 'hello image', False, 'creating', '----', datetime.utcnow(), True)
db.session.add(image)
db.session.commit()

print Platform.as_dict(plat)

'''
query = Platform.query.all()
for i in query:
    print(i.Name)

db.session.remove()