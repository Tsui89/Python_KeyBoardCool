__author__ = 'IBM-cuiwc'

import globalvalue

class Keymap():
    def __init__(self):
        self.coolid = globalvalue.COOLID
        globalvalue.COOLID += 1
        self.CoolKMap={}
    def AddKMap(self,key,*keyargs):
        self.CoolKMap[key] = keyargs
        print self.CoolKMap

    def On(self):
        pass
    def Off(self):
        pass
