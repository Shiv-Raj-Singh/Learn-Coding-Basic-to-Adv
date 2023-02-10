# make a dict '''                              EX--- 1
# '''x=int(input('enter a number 1-5  --'))
# d1={1:'mangal',
    # 2:'don',
    # 3:'shiv',
    # 4:'raj',
    # }
# print(d1[x,x])'''

        # FAULTI CALCULATER FOR FEW NUMBERS                 EX----  2

# x=(input('enter a operator which you want to do perform--'))                                        
# a=int(input('enter the num 1   '))
# b=int(input('enter the num 2   '))
# if x=='+':
#     if a+b==20:
#         print('25')
#     else:
#         print(a+b)
# elif x=='*':
#     if a*b==48:
#         print('85')
#     else:
#         print(a*b)
# if x=='-':
#     if a-b==50:
#         print('25')
#     else:
#         print(a-b)
                    # GUESS THE RIGHT NUMBER IN LIMITED TIME 
                    
number=49
x=int(input('guess a number-   '))
guess_time=1
game_over=False
while x!=49 or guess_time!=5:
    if x > number:
        print(f'your nuber is too big you have only 5 rounds in which you used {guess_time} rounds ')
        x=int(input("enter again your number is too big-  "))
        guess_time+=1
    elif x< number :
        print(f'your nuber is too low you have only 5 rounds in which you used {guess_time} rounds ')
        x=int(input("enter again your number is too low-  "))
        guess_time+=1
    else:
        if number==49:
            print('YOU WIN //') 
        elif guess_time==5:
            print('//UFF GAME OVER ')
        else:
            print('// GAME OVER //')   
    # x=int(input(' guess again-  '))
    
    game_over=True

