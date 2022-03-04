#get input from user

# name=input("Enter Your Name: ")
# age= int(input("Enter Your Age: "))
# print("Welcome "+name)
# year=str(2022-age)
# print("Your born year is "+year)

#LIST

# numbers=[1,2,3,4,5,6,7,8,9,10]
# print("Number[0]: ",numbers[0])
# print(numbers[1:10])
# print(numbers[1:5])
# print(numbers[:-3])
# print(numbers[2:-3])
# print(numbers[1:-1:1])
# print(numbers[2:1:-1])
# print(numbers[1:2:-1])
# print(numbers[9:2:-1])
# print(numbers[::1])

#list methods
numbers=(1,2,3,4,5,6,7,8,9,10)
# numbers.append(5)
# print(numbers)
# numbers.pop(5)
# print(numbers)
# numbers.insert(3,30)
# print(numbers)
# print(numbers.count(9))
# numbers.sort()
# print(numbers)
# del numbers
# a=[1,3,4,5,6]
# b=[2,5,6,7,8,9]
# v=a+b
# print(c)
# print(v)
print(numbers[7])

x=int(1)
y=int(2.8)
z=int(3)

print(type(x))
print(type(y))
print(type(z))
print(float(y))

a=1222222222222222222224
b=3.211111111111111111111
c=-45353
print(type(a))
print(type(b))
print(type(c))

e=15

print(int(e))
print(float(e))
print(str(e))

d=12E4
print(type(d))

f=3+5j
g=5j

print(type(f))
print(type(g))


wor={1:"one",2:"two",3:"three"}
man={(1,2,3) :"value",4:"0"}
print(man)
print("",wor)
print(man[4])
print("", "four" not in man )
wor.popitem()
print(wor)

#set

str1={1,2,3,4,5,6,7,8,9,10}
str2={1,2,3,4,5,6,7,8,98,10}
print(str1.union(str2))
print(str1.difference(str2))
print(str1.intersection(str2))
str2.update(str1)
print(str2)