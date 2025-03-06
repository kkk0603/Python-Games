#game for rock,paper,scissor
import time
import random


print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
name=input("Enter your name :: ")
print("Welcome",name,"to one of the best game you have played ever.")
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")


options=["rock","paper","scissor"]

draw=0
player=0
computer=0

time.sleep(2)
n=int(input(" Enter no of times you want to play :: "))

time.sleep(2)
print("Your Options are :: ",options)
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")

for i in range(0,n):
    time.sleep(1)
    userturn=input("Enter your choice ( rock,paper or scissors) ::")
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    comp_choice=random.choice(options)
    time.sleep(1)
    print("Computer choice is",comp_choice,".")
    time.sleep(2)


    if comp_choice=="rock" and userturn=="paper":
      computer+=1
      time.sleep(1)
      print("Hurray!! You won the round.")
    if comp_choice=="paper" and userturn=="rock":
      computer+=1
      time.sleep(1)
      print("Oppss! You Lose , Computer won the round.")
    if comp_choice=="scissor" and userturn=="paper":
      computer+=1
      time.sleep(1)
      print("Oppss! You Lose , Computer won the round.")
      
    if comp_choice=="rock" and userturn=="scissor":
      computer+=1
      time.sleep(1)
      print("Oppss! You Lose , Computer won the round.")
    if comp_choice=="paper" and userturn=="scissor":
      player+=1
      time.sleep(1)
      print("Hurray!! You won the round.")
    if comp_choice=="scissor" and userturn=="rock":
      player+=1
      time.sleep(1)
      print("Hurray!! You won the round.")
    if comp_choice==userturn:
      time.sleep(1)
      print("Its a tie .")
      draw+=1
      print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
time.sleep(2)
print("    ",name," your total score =",player)
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
time.sleep(2)
print("     Computer total score=",computer)
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
time.sleep(2)
print("     Number of tie matches =",draw)


print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
if computer>player:
    time.sleep(2)
    print("     Soryy BETTER LUCK Next Time ,Computer WINS .")

elif computer<player:
    time.sleep(2)
    print("     You are a Player",name," #You Won.")
else:
    time.sleep(2)
    print("     It's a DRAW .")
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")        



