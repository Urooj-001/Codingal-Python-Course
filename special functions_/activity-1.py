class myClass():
    __privVariable = 27

    def __privMeth(self):
        print("I'm in the class my Class")

    def hello(self):
        print("Private variable: ", myClass.__privVariable )

obj = myClass()
obj.hello()
obj.__privMeth()