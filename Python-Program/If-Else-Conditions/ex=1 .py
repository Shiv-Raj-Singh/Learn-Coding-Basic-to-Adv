winning_number=51
x=int(input("guess a lucky number "))
guess=1
game_over=False
while not game_over:
    if x==winning_number:
        print(f"you got the lucky number guessed after {guess} times ")
        guess+=1
        game_over=True
    else:
        if x<45:
            print("your number is too low ")
            guess+=1
            x=int(input("enter again a number your last is  a lowest number to lucky number  ="))
        else:
            if 51 < x  >45:
                print("your number just little bit low ")
                guess+=1
                x=int(input("enter a number again to biggest than to last number -"))
            else:
                if  51<x>57:
                    print("your number just few numbers bigger than to lucky number ")
                    guess+=1
                    x=int(input("enter a number just small to last number -"))
                else:
                    if x>57:
                        print("your number is so high to lucky number ")
                        guess+=1
                        x=int(input("guess another number smallest to last number - -"))
                        