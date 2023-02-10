# create a game for guessing numbers -
# import pdb
# pdb.set_trace()
import random
wn=random.randint(1,100)
x=int(input('enter a num- between 1-30 -- '))
guess=1
game_over=False
# while not game_over 
while not game_over :
    if x!=wn and guess==5:
        print('// off GAME  OVER  //')
        print(f'WINNING NUMBER IS {wn}')
        break
    if x==wn and guess==5:
        print(f" after {guess} times ")
        print('// YOU WON //')
        game_over=True
    elif x>wn:
        print('guess again too high ')
        x=int(input( f"enter gaain you used {guess} out of 9 -  "))
    else:
        print('too low ')
        x=int(input( f"enter gaain you used {guess} out of 9 -   "))
    guess+=1   
# if x!=wn and guess==5:
#     print('// YOU LOST //')
#     print(' PLAY AGAIN AFTER SOME TIME--')
    
