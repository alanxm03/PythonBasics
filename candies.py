candies_count=3
print(f"Available candies are {candies_count}")

inp=int(input("How many Candies do you want "))
if inp<=candies_count:
    for i in range(0,inp):
            print("Candies")
            candies_count-=1
else:
    print(f"Available Candies are {candies_count} But you entered {inp}")
    nxt=input("Continue or Exit:").lower()
    if nxt=="continue":
        for i in range(0,candies_count):
            print("Candies")
            candies_count-=1

    else:
        print("Thank You")
        exit
if(candies_count>0):
    print(f"Available Candies is {candies_count}")
else:
     print("Out of Candies")
    