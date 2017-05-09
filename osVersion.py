# -*- coding: utf-8 -*-
from sys import platform as pf
import socket

print pf
if pf == "linux" or pf == "linux2":
   print 'linux'
elif pf == "darwin":
   print 'max os'
elif pf == "win32":
   print 'windows'
else:
    print 'none'

lan = socket.gethostbyname(socket.gethostname())
if lan == '117.16.146.98':
    print '117.16.146.98'
else:
    print lan
