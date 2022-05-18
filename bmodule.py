# 7: Creating circular module dependencies
# We have two files, bmodule.py and cmodule.py, each of which imports the other, as follows:

import cmodule
from amodule import aMODULE


def f():
<<<<<<< HEAD
    return cmodule.e
	
print (f())
aMODULE.actionX()
=======
    return cmodule.g


print(f())

>>>>>>> 8bd440f1587a1ccf2099c3b716232ec3e7ab86f2

def cleanup(self):
    return
