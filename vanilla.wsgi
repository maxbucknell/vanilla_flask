activate_this = '/home/mpwb500/Envs/vanilla/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))
import sys
sys.path.insert(0, '/home/mpwb500/vanilla_flask')
from vanilla import app as application