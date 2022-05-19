# 7: Creating circular module dependencies
# We have two files, bmodule.py and cmodule.py, each of which imports the other, as follows:
import bmodule


def g():
    return bmodule.f


def e():
    return
