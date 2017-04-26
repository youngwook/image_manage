import sys

sys.stdout = sys.stderr
sys.path.insert(0, '/var/www/myproject/image_manage/image_manage')
sys.path.insert(0, '/var/www/myproject/image_manage')

activate_this = '/var/www/myproject/env/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

from image_manage import app as application