# number chaseing game
import random
guess_no=random.randint(1,100)
u_no=int(input("enter a number ="))
while u_no!=guess_no:
    if(u_no<guess_no):
        print("it is too low")
    if(u_no>guess_no):
        print("it is too high")
    u_no=int(input("enter a number ="))
print("you won")
