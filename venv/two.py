
#Class is blueprint for objects. Multiple objects can be created with a class
class PyClass:
    classattribute='Nitheesh'
    print("************** 9. Classes, Functions & Methods **************")
    #function inside classes are called methods.
    def mergetext(self,x,y):
        return self.classattribute + x+y.upper()
    @staticmethod
    def mergenumber(x,y):
    def mergenumber(x,y):
        return x+y
        #Self mandatory is required because to say refer to PyClass cuz u r a member of this class. Not because you are defined inside this PyClass. You refer to this
        #class using self. self word is just regular placeholder. can you any other variable.
        # The self first parameter is (mandatory parameter) is a reference to the current instance of the class, and is used to access attributes/methods that belongs to the class.
class PyClass1:
    classattribute='Nitheesh'
    print("************** 9. Classes, Functions & Methods **************")
    #function inside classes are called methods.
    def mergetext(self,x,y):
        return x+y.lower()
obj1=PyClass()
obj2=PyClass1()
print("Class attribute is : {}".format(obj1.classattribute))
print("calling methos in class and passing parms:- "+str(obj1.mergetext("Nitheesh","Bharadwaj")))
print("calling methos in class and passing parms:- {} ".format(str(obj1.mergetext("Nitheesh","Bharadwaj"))))
print(obj1.classattribute)
print(PyClass.classattribute)
print(PyClass().mergetext(" ITI ","SHUKLA"))
print(PyClass().mergenumber(1,2))

print(obj2.mergetext("KB","NL"))

class Pyclass2:
    classattribute=""
    def __init__(self,arg1):
        self.classattribute=arg1

