# #BOOL FALSE

# # print(bool(0))
# # print(bool(set()))
# # print(bool(dict()))
# # print(bool(""))
# # print(bool(list()))
# # print(bool(tuple()))


# #if condition

# # from ast import If


# # x=5
# # if x==5:
# #     print("x is 5")
# # print("Byee Byee")

# # #if..else 

# # x=5
# # if x>5:
# #     print("Success")
# # else:
# #     print("failure")

# # #nested if...else

# # x=30
# # if x==1:
# #     print("x is 1")
# # else:
# #     if x==2:
# #         print("x is 2")
# #     else:
# #         if x==3:
# #             print("X is 3")
# #         else:
# #             print("type between 1-3")

# # # elif condition(else if condition)

# # x=2
# # if x==1:
# #     print(x)
# # elif x==2:
# #     print(x)
# # elif x==3:
# #     print(x)
# # else:
# #     print("type btwn 1-3")

# # #POSITIVE OR NEGATIVE

# # n=int(input("Enter a integer: "))
# # if n>=0:
# #     print("POSITIVE INTEGER")
# # else:
# #     print("NEGATIVE INTEGER")

# # #ODD OR EVEN

# # m=int(input("Enter a Value: "))
# # if n%2==0:
# #     print("EVEN")
# # else:
# #     print("ODD")

# #GREATER OR LESSER

# # a=int(input("Enter a Value: "))
# # b=int(input("Enter b Value: "))
# # c=int(input("Enter c Value: "))
# # if a>b and a>c:
# #     print(a,"is GREATER")
# # elif b>c:
# #     print(b,"is GREATER")
# # else:
# #     print(c,"is GREATER")

# #for loop
# # values=[1,2,3,4,5]
# # for value in values:
# #     print(value)

# num=range(20)
# print(num)

# for v in "EMOTIONAL DAMAGE":
#     print(v)

# n=list(range(5,20,5))
# print(n)
# print(type(range(5)))

# for va in range(10):
#     print(id(va))

# x=[1,2,3]
# y=[1,2,3]
# z=x
# print(id(x[0]),id(y[0]))
# print(x is y, x is z)


# #while loop

# i=0
# while i<5:
#     print(i)
#     i+=1

n=[1,2,3,4,5]
a=b=n[0]
for i in n:
    if a<i:
        a=i
    if b>i:
        b=i
print("Max",a,"Min",b)