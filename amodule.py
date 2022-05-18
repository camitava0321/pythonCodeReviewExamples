#1: same module and filename

class aMODULE():
    def actionX():
        return True


#2: Misusing the __del__ method
import bmodule

class Bar(object):
    def __del__(self):
        bmodule.cleanup(self.myhandle)
        



def amodule(num):
    return "amodule "+str(num)
def aMODULE(num):
    return "aMODULE "+str(num)

        