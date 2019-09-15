from proj.settings.base import *

from proj.settings.production import *

try:
   from .local import *
except:
   pass
  
print("init of old settings")