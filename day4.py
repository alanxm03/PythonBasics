#Functions
#a function is defined using 'def' keyword
#creating first basic function'

def my_func():
    inp=input("Enter your name: ")
    print("Hey your name is "+inp)
# print(my_func())

def calc(x,y):
    x=int(x)
    y=int(y)
    print("\n1.Add\n2.Sub\n3.Mul\n4.div")
    s=input("Enter a Number ")
    if s=="1":
        print(f"{x}+{y} = ",x+y)
    elif s=="2":
        print(f"{x}-{y} = ",x-y)
    elif s=="3":
        print(f"{x}*{y} = ",x*y)
    elif s=="4":
        print(f"{x}/{y} = ",x/y)
    else:
        print("Enter Valid Number...")

# a,b=input().split()
# calc(a,b)

def mul(*a):
    # print(a)
    total=1
    if len(a)==1:
        total*=a[0]
        return total
    else:
        for i in a:
            total*=i
        return total
# print(mul(3,3,4))

#keyword Arrguments

def argg(name,age):
    print(f"Welcome {name}. Your age is {age}")
# argg(age=25,name="Alan")
# argg("Alan",age=25)


def studentDet(name,**k):
    print(name)
    print(k)

# studentDet("sn",age=12,std=7)

def shout(word):
    print(word)
sound = shout
speak = sound
# speak("Emotional Damage")

def hello():
    pass            #can be implemented later does not give error

def fact(x):
    if x==0:
        return 1
    return x*fact(x-1)
# print(fact(5))

#recurrsion function
def sum(x):
    if x==1:
        return 1
    return x+sum(x-1)
# print(sum(7))
# print(7+6+5+4+3+2+1)

#lambda(anonimize function)
x=lambda a:a+10
# print(x(5))

y=lambda a,b:a*b
# print(y(10,2))

def val(food):
    for x in food:
        print(x)
fruits=["apple","banana","cherry"]
# val(fruits)


#SCOPE#SCOPE#SCOPE#SCOPE#SCOPE#SCOPE#SCOPE#SCOPE#SCOPE#SCOPE#SCOPE#SCOPE#SCOPE#SCOPE#SCOPE#SCOPE

x=5
# print("Global x:", x)
# print("Global x:", id(x))

def glo():
    print("Local x:", x)
    print("Local x:", id(x))
# glo()


x=8

def check():
    x=6
    print("Local x:", x)
    print("Local x:", id(x))
# check()
# print("Global x:", x)
# print("Global x:", id(x))

#EXCEPTION ERROR RUNTIME/COMPILE TIME/LOGICAL ERROR

x=5
y=1
try:
    print("File Open")
    print(x/y)
except ZeroDivisionError:
    print("Cant divide by zero")
except ValueError:
    print("Cant take string as input")
except Exception as e:
    print("Invalid",e)
finally:
    print("File Close")
print("Bye")

#IMPORT#IMPORT#IMPO#IMPORT#IMPORT#IMPOrt
#random

# import random
from random import randint,shuffle
print(randint(0,10))
list1=[1,2,3,4,5,6,7,8,9,10]
shuffle(list1)
print(list1)

import function
function.question()

import random as r; from math import pi,sqrt,floor,ceil,cos,tan,sin

for i in range(5):
    print(r.randint(0,7))
print(sqrt(10))
