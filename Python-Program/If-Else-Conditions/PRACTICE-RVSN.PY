                                # FIND FECTORIAL OF A NUMBER
# from math import factorial
# num=int(input('enter a number-'))
# x=factorial(num)
# print(x)
    
# num=int(input('enter a number-'))
# def factorial(n):
#     if n==1:
#         return 1
#     elif n==0:
#         return 0
#     else :
#         return n*factorial(n-1)
# print(factorial(num))

# if num==1:
#     print('1')
# elif num==0 :
#     print('0')
# else:
#     t=1
#     for i in range(num):
#         i+=1
#         t=t*i
#         print(t)
# print(f'factorial of {num} is {t}')

#                                          CREATE A FIBBONACCI SERIES 

n=int(input('enter the numbers thats between find fibbonaci numbers/series--'))
x=0
y=1
if n==0:
    print(x)
elif n==1:
    print(y)
else:
    for i in range(2,n):
        t=x+y
        print(t,end=',')
        x=y
        y=t
    
# --# ARMSTRONG NUMBERS A NUMBER --15 NUMBER OF DOGIT 2 1**2(DIGIT) + 5**2  EQUAL TO NUMBER 15 THEN ITS ARMSTRONG NUMBER--
    
# def arm_strong_number(n):
#     a=n
#     x=len(str(n))
#     y=0
#     while n!=0:
#         b=n%10
#         y=y+(b**x)
#         n=n//10
#     if y==num:
#         print('its an arm-steong-number')
#     else:
#         print('its not an armstrong number')
        
# num=int(input('enter a number --'))
# arm_strong_number(num)
    
# num=int(input('enter a num--'))   
# def fac__num(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return n*fac__num(n-1)
# print(fac__num(num))
    
# def fibbo_series(n):
#     n1=0
#     n2=1
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     # n3=n1+n2
#     else:
#         for i in range(2,n):
#             n3= n1+n2
#             print(n3 ,end=',')
#         n1=n2
#         n2=n3
# (fibbo_series(num))
        
    
        