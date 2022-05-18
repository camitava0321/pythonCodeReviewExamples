# 1: same module and filename

import bmodule


def aMODULE():
    return True


# 2: Misusing the __del__ method


class Bar(object):
    def __del__(self):
        bmodule.cleanup(self.myhandle)
