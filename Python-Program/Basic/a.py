'''from random import random 
import random
winning_number=random.randint(1,100)'''

'''winning_number=15
x=int(input("guess a number-"))
y=1
game_over =False
while not game_over:
   if x==winning_number:
      print(f"you guess the right nuber after {y}")
      game_over=True
   else:
      if x<winning_number:
         print("your number is too low please guess agaim a number which bigger than to it- ")
         y+=1
      else:
         print("your number is too high please guess agaim a number which less than to it")  
         x=int(input("guess again - "))
         y+=1
'''

winning_number=7
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
            x=int(input("guess try again "))

