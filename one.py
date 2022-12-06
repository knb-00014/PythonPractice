print("My 1st print in Python")

x="Nitheesh"
y='Bharadwaj'
print(x+" This is in DOuble quotes"+' From Now its single Quote'+y)

flt=10.23
print("flt" )
print(isinstance(flt,float))

strdata = "Nitheesh Bharadwaj"
print(strdata.upper())
print(strdata.lower())
print(strdata.islower())
print(strdata.isupper())
print(strdata.isnumeric())
print(strdata.count("e"))
print(strdata.startswith("N"))
print(strdata.endswith("B"))
print(len(strdata))
print(strdata.__len__())
#Comment
'''Comment
Multi'''
#Dyamically Types. Scala is weakly typed.
n1=100
n2=120
print(n1+n2)
n2="Nitheesh"

#Python is strongly typed. Meaning int+string in Python is error. In Scala it concatinates.

'''COnditional Structures'''


a=50;b=20;c=30
if(a==b==c):
    print("All are equal")
else:
    print("Not equal")
print("Came from out of loop")

#Lambda

lst = [5,4,3,2,1]
for i in  reversed(lst):
    print(i)
'''
SCALA
var lst=List(1,2,3,4,5)
for ( I <- lst)
println()
'''

c1=["NItheesh is ","Iti is "]
c2=["Good"," Not Bad","Seggsy"]
for x in c1:
    for y in c2:
        print(x,y)

c3=0
while(c3<5):
    print(c3)
    c3=c3+1
c3=0
while c3 < 10:
    c3=c3+1
    if c3==5:
        continue
    print(c3)

print("Collections***************************")

# Scala Collections - Seq,Array/List, Tuple,Map,Set
#Python - List Tuple Dictionary, Set

print("List is mutable")

List1=["a","b","c"]
print(List1)
List1.remove('b')
print(List1)
List1.insert(1,'bb')
print(List1)
List1[2]='CC'
print(List1)
List1.reverse()
print(List1)
print(List1)
List1.clear()
print(List1)
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
lst = [5,4,2,3,1]
print(lst)
print(weekdays)
print("slicing a list")
print(lst[0:3])
weekdays=weekdays.__add__(lst)
print(weekdays)
print(weekdays.count(5))
print(len(weekdays))
#single column - list
#single row - tuple
#all columns all rows - list(tuples)

print("Tuples (immutable) - () - similar to Scala")
#Same Syntax in Scala and Python
# Cant iterate in Scala. Begin from 1
# Can iterate in Python.begin 0

tup1=('Nithes','Bhaaradwaj','K')
print(tup1)
for i in tup1:
    print(tup1)

print(tup1[0])
print(len(tup1))
print("""print("tuple doesn't support any add/update/delete operation")""")
#tup1[0]='k'
print('Workaround is convert to list and do the operation')
print(tup1)
tuplist=list(tup1)
print(tuplist)
tuplist.remove('K')
print(tuplist)
tuplist.insert(1,'k')
print(tuplist)

print("Set (mutable) - {} ")

my_set={5,4,3,3,2,22,1,35,33,35}
print(my_set)
my_set.add(6)
print(my_set)
my_set_list=list(my_set)
print(my_set_list)
print(my_set.intersection(my_set))
my_set.remove(3)
print(my_set)
my_set.add(62)
print(my_set)
my_set2={1,2,3,4,5}
my_set.update(my_set2)
print(my_set)
my_set3={1,2,3,4,5,6,7,8,9,10}
my_set.update(my_set3)
print(my_set3)

print("Dictionaries (mutable) - {k:v, k:v}")

# When to go for tuple and when with dictionary - its equivalent to the tradeoff between csv and json / sql(mysql) vs nosql(hbase/es)
# Tuple - index/Positional access, storing fixed number of unbounded elements (type and the name are not bounded), eg. fixed fields records
# dictionary - key based access, variable number of bounded elements (type and name are bounded) eg. dynamic fields records
print("Dictionaries in python is Map in scala")

my_tup=("Nitheesh","Bharadwaj",1)
my_dict={'firstname':'Nitheesh','lastname':"Bharadwaj","Rank":1}
print(my_dict)
my_dict["city"]="vizag"
print(my_dict)
my_dict["city"]='NOIDA'
print(my_dict)
print(my_dict.__delitem__("Rank"))
print(my_dict)
print(my_dict.pop("city"))
print(my_dict)
print(my_dict.keys())

my_dict={'firstname':'Nitheesh','lastname':"Bharadwaj","Rank":1}
print("looping dictionary")
print("Printing keys:-**********")
for i in my_dict.keys():
    print(i)
print("Printing values:-**********")
for i  in my_dict.values():
    print(i)

print("converting my_dict to items type to access list of tuples for looping")
print(my_dict.items()) #items return us List(Tuples)

print("Printing keys and values")
for i,j in my_dict.items():
    print('i','j')
    print(i,j)




print("Complex tuple1 - tuple(list,dictionary,tuple)")
print("Hive equivalent - struct(array<int>,map<a:string,b:String>,struct)")
tup11 = (['SWE','SSE'], {'Name': 'Irfan','Age':40}, (1,10000,'Chennai'))
tup12 = (['Trainee','SWE','Analyst'], {'Name': 'Mydeen','Age':30,'Hometown':'Madurai'}, (2,15000,'Chennai'))
print(tup11[0][1])#SSE
print(tup11[1]['Name'])#Irfan
print(tup11[2][2])#Chennai

#{"results":
# [{"gender":"male","name":{"title":"Mr","first":"Lucas","last":"Gallardo"},"location":{"street":{"number":49,"name":"Ronda de Toledo"},"city":"Bilbao","state":"Navarra","country":"Spain","postcode":72759,"coordinates":{"latitude":"-24.1241","longitude":"-42.9993"},"timezone":{"offset":"+5:45","description":"Kathmandu"}},"email":"lucas.gallardo@example.com","login":{"uuid":"a4c0f1db-35ef-43b9-9d23-b1da970f4876","username":"blackduck720","password":"spank","salt":"ov40nTLe","md5":"2d2a37e544c2423dabd30e45b04d01de","sha1":"2c6398b2cd82becb356a624b661978c9c0ae699c","sha256":"e26278657a9c3d9b17572dd14c75e402deebef7ff25600981c923a8e0b307759"},"dob":{"date":"1951-01-05T20:37:44.406Z","age":71},"registered":{"date":"2016-09-08T07:29:59.842Z","age":6},"phone":"954-092-544","cell":"671-763-895","id":{"name":"DNI","value":"97111064-H"},"picture":{"large":"https://randomuser.me/api/portraits/men/65.jpg","medium":"https://randomuser.me/api/portraits/med/men/65.jpg","thumbnail":"https://randomuser.me/api/portraits/thumb/men/65.jpg"},"nat":"ES"}
# ,{"gender":"female","name":{"title":"Mrs","first":"Elisa","last":"Gallardo"},"location"
# .:{"street":{"number":49,"name":"Ronda de Toledo"},"city":"Bilbao","state":"Navarra","country":"Spain","postcode":72759,"coordinates":{"latitude":"-24.1241","longitude":"-42.9993"},"timezone":{"offset":"+5:45","description":"Kathmandu"}},"email":"lucas.gallardo@example.com","login":{"uuid":"a4c0f1db-35ef-43b9-9d23-b1da970f4876","username":"blackduck720","password":"spank","salt":"ov40nTLe","md5":"2d2a37e544c2423dabd30e45b04d01de","sha1":"2c6398b2cd82becb356a624b661978c9c0ae699c","sha256":"e26278657a9c3d9b17572dd14c75e402deebef7ff25600981c923a8e0b307759"},"dob":{"date":"1951-01-05T20:37:44.406Z","age":71},"registered":{"date":"2016-09-08T07:29:59.842Z","age":6},"phone":"954-092-544","cell":"671-763-895","id":{"name":"DNI","value":"97111064-H"},"picture":{"large":"https://randomuser.me/api/portraits/men/65.jpg","medium":"https://randomuser.me/api/portraits/med/men/65.jpg","thumbnail":"https://randomuser.me/api/portraits/thumb/men/65.jpg"},"nat":"ES"}]
# ,"info":{"seed":"1934b3808d5cc6aa","results":1,"page":1,"version":"1.3"}}

print("Complex Tuple2 - tuple(familyid:int,familyname:str,familymembers:list[dict{k:v,k:v,k:dict{k:v,k:v}}])")
complextup=(1,
            "Madison's Family",
            [{"gender":"male","Relation":"self","personalinfo":{"title":"Ms","name":"Madison"}},
             {"gender":"female","Relation":"spouse","personalinfo":{"title":"Mrs","name":"Elisa"}},
             {"gender":"female","Relation":"daughter","personalinfo":{"title":"Miss","name":"Hanna","hobby":"book reading"}},
             {"gender":"male","Relation":"son","personalinfo":{"title":"Master","name":"Dave","schooling":True}}])

print("id is "+str(complextup[0]))
print("Family name is " + str(complextup[1]))
print("gender of first list element is " + complextup[2][0]["gender"])
print("relation of first list element is " + str(complextup[2][0]["Relation"]))
print("personalinfo of the first list element is " + str(complextup[2][0]["personalinfo"]))
print("personalinfo title of the first list element is " + str(complextup[2][0]["personalinfo"]["title"]))
print("personalinfo name of the first list element is " + str(complextup[2][0]["personalinfo"]["name"]))
print("personalinfo name of the second list element is " + str(complextup[2][1]["personalinfo"]["name"]))
print("personalinfo hobby of the third list element is " + str(complextup[2][2]["personalinfo"]["hobby"]))
print("personalinfo schooling info of the fourth list element is " + str(complextup[2][3]["personalinfo"]["schooling"]))


print("*********************************METHODS")

# Python is dynamically typed.So need of giving input type in method like Scala.

def add1(a,b):
    print(a)
    print(b)
    print(a+b)
    return a-b

print(add1(2,3) )

# Lambda means using across in same function. This is not for across platform. unlike above.

anonymus_lamba = (lambda x,y:x-y)
#Lamba in Scala. Val anonymus_lambda = (x:Int,y:Int)=>x-y
#Why need Lambda keyboard.

print(anonymus_lamba(2,3))

print("Difference {}".format(anonymus_lamba(5,3)))

lst11=[1,2,3,4,5]

res=map(lambda x:x+100,lst11)
for i in list(res):
    print(i)


print("********HIGHER ORDER*************************")

def even_filtering(f):
    if(f%2)==0:
        return True
    else:
        return False

print(even_filtering(2))

filter_list=[1,2,3,4,20,30,50]

print("higher order function eg. with even list of values by calling lambda function inside the filter function")

xh = filter(lambda x:(x%2==0),filter_list)
print(xh)
print(list(xh))

print("higher order function eg. with filtered even list calling normal named function: ")

xh1=filter(even_filtering,filter_list)
print(list(xh1))












