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

winning_number=51
x=int(input("enter a lucky number -"))
y=0
game_over=False
while not game_over :
    if x==winning_number:
        print(f"you got the lucky number after {y} times ")
        y+=1
        game_over=True
    else:
        if x<35:
            print("your number is too low")
            y+=1
            x=int(input("enter again babu your number  "))
        elif x>winning_number:
            print("your number so high baby ")
            y+=1
            x=int(input("enter another times "))
        elif 35<x>winning_number :
                print("your number is close try again baby")
                y+=1
                x=int(input("enter again baby="))
        else :
            print("your number is too high bro ")
            y+=1
            x=int(input("enter again bro  "))

