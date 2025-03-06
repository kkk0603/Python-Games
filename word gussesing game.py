# program for hang man word gusseing game
import random
name=input("enter your name? ")
print("get ready",name," to play game ")
a=random.choice(["scet","whispering","windows","bat","football","chess","badminton","cricket","russia","USA","india","surat","gujarat","delhi","pizza","burger"])
gusses=" "
turns=10
while turns>0:
    failed=0
    for j in a:
        if j in gusses:
            print(j,end=" ")
        else:
            print("_",end=" ")
            failed+=1
    print()
    mygusses=input("enter your first gusses =")
    gusses+=mygusses
    if mygusses not in a:
        turns-=1
        print("wrong")
        print("you have",turns,"turns left")
    if turns==0:
        print("you loss")
    if failed==0:
        print("you won")
        break
    
