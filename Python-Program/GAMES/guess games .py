from random import random
import random
winning_number=random.randint(1,10)
x=int(input("guess a number-"))
y=1
game_over=False
for in not game_over:
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
            x=int(input("guess try again "))
                        