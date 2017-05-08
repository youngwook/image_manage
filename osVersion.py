# -*- coding: utf-8 -*-
from sys import platform as pf

print pf
if pf == "linux" or pf == "linux2":
   print 'linux'
elif pf == "darwin":
   print 'max os'
elif pf == "win32":
   print 'windows'
else:
    print 'none'