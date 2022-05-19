# 7: Creating circular module dependencies
# We have two files, bmodule.py and cmodule.py, each of which imports the other, as follows:

import cmodule
from amodule import aMODULE


def f():
    return cmodule.g


print(f())


def cleanup(self):
    return
