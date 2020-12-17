

class Protected_And_Private:
    # when the class is instantiated, this method creates a property for it called '__protectedVar'
    def __init__(self):
        self._protectedVar = "This is a protected var"
    # when the class is instantiated, this method creates a property for it called '__privateVar'
    def __init__(self):
        self.__privateVar = "This is a private var"
    # this method prints the value stored in '__privateVar'
    def getPrivate(self):
        print(self.__privateVar)
    # this method allows one to change the value of '__privateVar'
    def setPrivate(self, private):
        self.__privateVar = private

obj = Protected_And_Private()
