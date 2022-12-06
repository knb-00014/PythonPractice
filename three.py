print("************** 10. OOPS in Python: ****************")
print(" ************** A) Polymorphism (Function Overloading) **************")
# Polymorphism is creating an similar named entity to represent different behaviours at different scenarios
# method names are same but purposes are different for different scenarios
# polymorphism can be applicable at built-in function levels as well. "len" is a classic example
# "len" can be applied on string, list, dictionary, etc. function name is same but usage is different as per data type

#Function Overloading with difference in type of arguments
print("User defined function with same name but different in data type")
print("Duck typing")
#Using Duck Typing, we do not check types at all. Instead, we check for the presence of a given method or attribute
#“If it looks like a duck and quacks like a duck, it’s a duck”
print("Builtin function with same name but different in data type (Duck typing)")
print(len("Python"))
print(len(["Python", "Java", "Scala"]))
print(len({"Name": "Inceptez", "City": "Chennai"}))

def calc(a,b,c):return a+b+c
print(calc(10,20,30))
print(calc("inceptez ","tech"," pvt ltd"))

print("Ducktyping + Function Overloading with difference in number of arguments + Closure example")
lst = [5,4,2,3,1] #Closure
def func1() :
    if lst.count(6) == 1:
        print("method if block")
    elif lst.count(5)==1:
        print("method elif block")
    else:
        print("method else block")

func1()

def func1(arg1:int):
  print ("method with one int argument")

func1(10)

def func1(arg1:str):
  print ("method with one str argument")

func1('hello method')