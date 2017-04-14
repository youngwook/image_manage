from image_manage import app as application
import sys

sys.path.insert(0, '/root/test/image_manage')

activate_this = '/root/test/bin/activate_this.py'
exec(activate_this, dict(__file__=activate_this))

