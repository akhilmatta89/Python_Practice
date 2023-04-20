# This the global namespace
var = 1

class students():

    def class_1(self):
        global var2 #This is local namespace
        var2=2
        print(var2)

inits = students()
inits.class_1()
print(var2)
