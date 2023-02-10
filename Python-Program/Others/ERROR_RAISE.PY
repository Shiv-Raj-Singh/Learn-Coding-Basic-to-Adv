# while True:
#     try:
#         x=int(input("enter your age -"))
#         # break
#     except ValueError:
#         print('you entered wromg data types you should entered must be int data type....')
#     except:
#         print("invalid syntax")
#     else:
#         print(f"user input the numberof age is {x}")
#         break
#     finally:
#         print('finallyu continue---')
        
# if x>18:
#     print("you are above 18")
# else:
#     print("your age below in 18")

# def divide(a,b):
#     try:
#         print("aruments must be in int ")
#     except TypeError:
#         raise ZeroDivisionError
#     print(' you cant divide by zero 0')
#     return a/b
# print(divide(9,0))
                                                # DEBUGGING 
                                                
# import pdb
# pdb.set_trace()
# x=input("enter your age=")
# y=input('enter your name--')
# z=f'the age of {y} is {x}'
# print(z)
# a=int(x)+5
# # print(a)
# print(f'after 5 years the age of {x} will be {a}')
    
f=open("newfile.txt","x")
