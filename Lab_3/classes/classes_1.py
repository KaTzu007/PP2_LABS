class String:
    def getString(self):
        self.string = input()
    
    def printString(self):
        print(self.string.upper())

user = String()
user.getString()
user.printString()
