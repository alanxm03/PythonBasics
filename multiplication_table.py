import random
no=[1,2,3,4,5,6,7,8,9,10]
inp=int(input("\tEnter the table Number: "))
random.shuffle(no)
count=0
for i in range(0,10):
   val= int(input(f"{no[i]} X {inp} = "))
   if val==no[i]*inp:
       print("Correct\n")
       count+=1
   else:
       print("Incorrect\n")
print("Total Correct Answer: ",count,"/10")

