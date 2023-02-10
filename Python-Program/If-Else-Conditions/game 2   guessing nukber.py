#  game for guessing right number 
'''winning_number=7
x=int(input("guess a number-"))
y=1
game_over=False
while not game_over:
    if x==winning_number:
        print(f"hey you won you guessed right numbers in {y} times ")
        game_over=True
    else:
        if x<winning_number:
            print("too low")
            y+=1
            x=int(input("guess again  "))
        else:
            print("too high ")    
            y+=1
            x=int(input("guess try again "))'''

'''winning_number=51
x=int(input("enter a lucky number -"))
y=0
game_over=False
while not game_over :
    if x==winning_number:
        print(f"you got the lucky number after {y} times ")
        y+=1
        game_over=True
    else:
        if x<=35:
            print("your number is too low")
            y+=1
            x=int(input("enter again babu your number  "))
        elif 35<x>winning_number:
            print("your number just low baby ")
            y+=1
            x=int(input("enter another times "))
        elif 59<x>65:
                print("your number is close just high try again baby")
                y+=1
                x=int(input("enter again baby="))
        else :
            if 65<x>100:
               print("your number is too high bro ")
               y+=1
               x=int(input("enter again bro  "))

'''
from ast import If
import random 
winning_number=random.randint(1,199):
x=int(input("enter a lucky nim="))
guess=0
game_over=False
while not game_over:
    if x==winning_number:
        print(f"your number is right after {guess} times")
        guess+=1
        x=int(input("guess again-"))
    else:
        If x<winning_number:
            print("your number is too low -")
        else:
            print("too high=")
    guess+=1
