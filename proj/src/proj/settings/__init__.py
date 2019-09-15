from .base import *
print("init of new setting")
from .production import *

try:
   from .local import *
except:
   pass
  
print("init of new settings")
   