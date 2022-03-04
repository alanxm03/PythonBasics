

# qn1=input("What is Apple Color?\n a. Orange\n b.Blue\n c.Yellow\n d.Red\n")
# if qn1=="d" or qn1=="D":
#     print("Correct")
# else: 
#     print("Wrong")

# qn1=input("What is Mango Color?\n a. Orange\n b.Blue\n c.Yellow\n d.Red\n")
# if qn1=="a" or qn1=="A":
#     print("Correct")
# else: 
#     print("Wrong")

# qn1=input("How many wheels does car have?\n a. 3\n b.2\n c.4\n d.1\n")
# if qn1=="c" or qn1=="C":
#     print("Correct")
# else: 
#     print("Wrong")

# qn2=["1.What is a Fruit? \na.Carrot \nb.Brinjal \nc.Mango \nd.Onion","1.What is a Vegetable? \na.Apple \nb.banana \nc.Onion \nd.Orange"]
# ans=["c","c"]
# for val in range(0,len(qn2)):
#     print(qn2[val])
#     n=input()
#     if ans[val]==n:
#         print("Correct")
#     else:
#         print("Wrong")

# a={"1.What is a Fruit? \na.Carrot \nb.Brinjal \nc.Mango \nd.Onion":"c","1.What is a Vegetable? \na.Apple \nb.banana \nc.Onion \nd.Orange":"c"}
# for i in a:
#     print(a.viewkeys())
#     # n=input()
#     # if n==


# sk=1234
# c=0
# for i in range(3):
#     inp=int(input("Enter Secret Key "))
#     if inp==sk:
#         print("You win")
#         break
#     else:
#         print("Retry Again")
#         c+=1
# if(c==3):
#     print("You Loose")
l=[]
for i in range(2000,3200):
    if i%7==0 and i%5!=0:
        l.append(str(i))
print(','.join(l))

