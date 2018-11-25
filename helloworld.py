####if else
if 5 < 2:
    print("hello world")
else:
    print("no hello")

####strings
a= "hello string"
print(a)
print(a[4])
print(a[2:8])
print(len(a))

####taking input

"""print("enter a and b")
a=input()
b=input()
print(a)"""

####lists brackets are square,has indexes,can be modified

fruits= ["apple","banana","grapes"]
print(fruits)
print(fruits[1])
fruits[1]="pineapple"
print(fruits)

for x in fruits:
    print(x)

if x in fruits:
    print("yepp")

print(len(fruits))

####tuples brackets are the curved,has indexes, cant modify but can add

items=("pen","pencil","book")
print(items)
   #items[1]="paper", tuples cant be altered

####set brackets are flower,no indexes,cant modify but can add

pizzaset={"paneer","onion","capsicum"}
print(pizzaset)
print("onion" in pizzaset)
print("banana" in pizzaset)

####dictionary like a map and can be created like a JSON object

carsdict ={
    "white" : "bmw",
    "black" : "audi",
    "cream" : "volvo"
}

print(carsdict)
print(carsdict["white"])
#print(carsdict["volvo"]) #error coz no key volvo

for x in carsdict:
    print(x)

for x in carsdict.keys():
    print(x)

for x in carsdict.values():
    print(x)

for x,y in carsdict.items():
    print(x, y)

####if and elif and else
a = 20
b = 30
if a > b:
    print("a>b")
elif b > a:
    print("b>a")
else:
    print("equal")

####while break and continue

i = 2
while(i):
    i+=1
    if i==3:
        continue
    if i==7:
        break
    print(i)
    
####for loop

for x in "hello":
    print(x)

for x in range(2,10,2):
    print(x)

for x in range(3):
    for y in range(3):
        print(x,y)

####functions

def helloWorld(name):
    print("hello "+ name)

helloWorld("venkatesh")

def factorial(num):
    if num>0:
        return num*factorial(num-1)
    else:
        return 1

print(factorial(5))


####lambda

x = lambda a: a*2
print(x(5))

####iterators

fruits = ["apple","mango","banana"]
myiter=iter(fruits)
print(next(myiter))
print(next(myiter))

####modules

import mymodule

print(mymodule.add(10))
print(mymodule.sub(10))
print(dir(mymodule))

from mymodule import sub
print(sub(20))

####handling json

import json

jsonvar = '{"name":"hello","id":"20"}'
dictvar = json.loads(jsonvar)
print(dictvar["id"])

fruits = ["apple","mango","banana"]
print(json.dumps(fruits))

####using pip

import camelcase

c = camelcase.CamelCase()

txt = "hello camel"

print(c.hump(txt)) 


####file handling

f=open("myfile.txt")
print(f.read())
f=open("myfile.txt") #coz the pointer moves to the end of file
print(f.readline())
f=open("myfile.txt")
print(f.read(5))

f=open("myfile.txt","a")
f.write("hello rookie")

f=open("myfile2.txt","w")
f.write("hello noobs")






