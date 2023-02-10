# print $ by inputs collum and row both have equal $
# for example --
#         '''
#              $ $ $ $
#              $ $ $ $
#              $ $ $ $
#         '''
#######################################################################################

x=5
for i in range(1,x+1):
    print(x*' $')

"""
Print $ with by incresing order like in first time 1 next 2 and untill
# $ will not print equal to N numbers
"""

# x=5
# for i in range(1,x+1):
#     print(i*' $')

"""Print $ with by Decresing order like in first time N $  next time N - 1 and untill 
# $ will not print equal to 1"""

# x=5
# for i in range(x+1 , 0, -1):
#     print(i*' $')

""" Print # increasing order till N times after decresing order till where from Start -
like -- # 
        # #
        # # #
        # #
        #
"""

# N = int(input('Enter the Number of rows-'))
# for i in range(N):
#     print(i*' #')
# for j in range(N-j):
#     print(j*' #')
#
# for i in range(N):
#     print("6"*i)

''''
print the number by row number like we have three row 
    1
    2 2
    3 3 3
'''
#
# for i in range(1+1):
#     for j in range(i):
#         print(i, end=' ')
#     print()
#

''' for print --
Expected Output: 
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
'''

# for i in range(5 + 1, 1, -1):
#     for j in range(1,i):
#         print(j, end=' ')
#     print()


""" print odd number * in each row 
 *
 * * *
 * * * * *
"""
# N = int(input('enter the number --'))
# for i in range(N+N):
#     if i%2!=0:
#         print('* '*i)





''' print for 
Input: 5

Output:

    *
   ***  
  *****
 *******
*********

'''

# N = int(input('enter the number --'))
# for i in range(N):
#     print("* " * i)
# for i in range(N, -1, -1):
#     print("* " * i)

'''
Input: 5

Output:
1 
0 1 
1 0 1
0 1 0 1 
1 0 1 0 1
'''
# x=0
# y=1
# for i in range(N):
#     for j in range(i):
#         if i % 2 != 0 or j%2!=0:
#             print(y,end=' ')
#         else:
#             print(x,end=' ')
#     print()
#



# k = 1
# for i in range(N + 1):
#     for j in range(1, i + 1):
#         print(k, end=' ')
#         k += 1
#     print()

#
# for i in range(N + 1):
#     a = 65
#     for j in range(1,i+1):
#         abc = chr(a)
#         print(abc, end='')
#         a=a+1
#     print()


# for i in range(N):

    # for j in range(0, N-i-1):
    #     print(end=" ")
    # for j in range(0,2*i + 1):
    #     abc = 65
    #     p = chr(abc)
    #     print(p , end='')
    #     abc+=1
    # print()

# for i in range(N):
#     for j in range(N-i-1):
#         print(end=' ')
#     for j in range(i+1):
#         print(i+1,end='')
#
#     print()

# a = str(N)
# # arr = a.split('')
# # .split('')
# # print(arr)
# total = 0
# for i in a:
#     print(i)
#     # if N%i== 0:
#     #     total += 1
#
# print(total)

# print(str(N)[::-1])


#  ARMSTRONG NUMBERS

# x = str(N).split()
# total = 1
# for i in x:
#     print(i)
#     a = int(i) ^ len(x)
#     print(a)
#     total += a
# if total == N:
#     print('Yes')
# else:
#     print('No')


# for i in range(N):
#     for j in range(i+1):
#         print('*',end="")
#     for j in range(N-i-1):
#         print(end=' ')
#     for j in range(N-i-1):
#         print(end=' ')
#     for j in range(i+1):
#         print('*',end="")
#     print()

# for i in range(N):
#     for j in range(N-i):
#         print('*', end="")
#     for j in range(i):
#         print(end=' ')
#     for j in range(i):
#         print(end=' ')
#     for j in range(N - i):
#         print('*', end="")
#     print()

# for i in range(N):
#     for j in range(N-i-1):
#         print(end='  ')
#     for j in range(i+1):
#         print('*',end=' ')
#     print()
# for i in range(N):
#     for j in range(i):
#         print(end='  ')
#     for j in range(N-i):
#         print('*', end=" ")
#     print()


# for i in range(N,0,-1):
# #     for j in range(i,0 ,-1):
# #         print('*',end=' ')
#     # for j in range(N,i,-1):
#     #     print(end='  ')
#     # for j in range(N,i,-1):
#     #     print(end='  ')
#     for j in range(i,0,-1):
#         print('*',end=' ')
#     print()
# for i in range(N):
#     # for j in range(i + 1):
#     #     print(j + 1, end=' ')
#     for j in range(i,N):
#         print(end="  ")
#     for j in range(i + 1):
#         print(j + 1, end=' ')
#     print()

# def hello(x):
#     if x == 0:
#         print(x)
#     else:
#         print(x^3 + hello(x - 1))
#
# print(hello(N))





