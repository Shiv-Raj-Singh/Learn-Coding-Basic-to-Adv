# guessing a lucky number -
winning_number=52
x=int(input("enter a lucky number-"))
guess=1
game_over=False
while not game_over:
    if x==winning_number:
        print(f"you got a right number after {guess} times ")
        guess+=1
        game_over=True
    else:
        if x<winning_number:
            print("your number is so high ")
            guess+=1
            x=int(input("enter again i hope you guess a right number "))
        else:
            print("your number is too low ")
            guess+=1
            x=int(input("enter a number again "))

