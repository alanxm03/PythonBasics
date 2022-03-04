from dataclasses import replace
import random
def words():
    key=['L', 'Z', 'P', 'Z', 'E', 'U', 'S']
    word=["puzzles","puzzle","pulse","plus","use","up"]
    count=0
    i=0
    while i<=len(key)-1:
        print(f"...Your{i} Chance....")
        random.shuffle(key)
        print(" ".join(key))
        inp=input("~ ")
        if(inp in word):
            print('Correct')
            word.insert("ioo",inp)
            count+=1
            print("Correct answer: ",count)
        else:
            print("Wrong")
            print("Correct answer: ",count)
            
        i+=1
words()
   # for i in range(len(word)):
    #     random.shuffle(key)
    #     print(" ".join(key))
    #     ans=input("-> ").lower()
    #     if(ans in word):
    #         print("Passed")
    #         word[i].replace(ans,"i")
    #         count+=1
    #     else:
    #         print("NOPE")
    # print(count)  