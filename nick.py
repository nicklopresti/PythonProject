class inputString:
    def _init_(self):
        self.s = ""
    def getString(self):
        self.s = raw_input()
    def printString(self):
        print self.s.upper()



strObj = inputString()
strObj.getString()
strObj.printString()
        
        
