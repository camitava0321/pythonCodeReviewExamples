#1: same module and filename

def aMODULE():
    return True


#2: Misusing the __del__ method
import bmodule

class Bar(object):
    def __del__(self):
        bmodule.cleanup(self.myhandle)