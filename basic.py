#basics

print()# ()->method

print("Hello World")# (ARGUMENTS) => ("HELLO WORLD")

print(type(5)) #type->prints the type of data

print('Hello \"World\"')#way1 to print a word in quotes inside a string value

print('Hello "ALAN"') #way2 to print a word in quotes inside a string value

a=5 #variable dec and assigning val
b=4
print(a,b)

print(id(a),id(b))#prints the location of a and b

a=5
b=10
print(a,b)

print(id(a),id(b))#prints the location of a and b


#Operators
print(a,"+",b,"=",a+b)
print(a,"-",b,"=",a-b)
print(a,"*",b,"=",a*b)
print(a,"/",b,"=",a/b)
print(a,"//",b,"=",a//b)


i=1j#complex
print(type(i))
#escape sequence

print('I\'am Studying\r"python"')
print('I\'am Studying\b"python"')


#to get the keyords
import keyword as k
print(k.kwlist)
print(len(k.kwlist))

#datatypes
print(type(1))
print(type(1.0))
print(type('a'))
print(type("alan"))
print(type(True))
