# DIFFRENCE BETWEEN RETURN AND PRINT 

'''def odd_even(x):
    if x%2==0:
        return( "Even")
    else:
        return ("odd")
z=int(input("enter a num-"))    
    
print(odd_even(z))'''

# define a program on a function which takes two numbers from users and return greater in them-
'''
def myFunc(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
        
print(myFunc(114,151,132))'''




# print a list in which print sqaure of numbers
'''
def square_list(l):
    squ=[]
    for i in l:
        squ.append(i**2)
    return squ
# num=[1,2,3,4,5,6,7,8] 
num=list(range(9))  
print(square_list(nu'''

# print the reverse list 





# def reverse_list(l):
    # l,reverse() use reverse method 
    # return l[::-1]  use slicing method 
    #  ude pop and append 
    # print two list in which print numbets odd even sparately 
    # '''even=[]
#     for i in l:
#         if i%2==0:
#             even.append(i)
#         else:
#             odd.append(i)
#     out= [even,odd]
#     return out   
# odd=[]
    
        # xyz=l.pop()
        # rvs.append(xyz)
#     # return rvs
# num=[1,2,3,4,5,6,7,8,9]
# print(reverse_list(num))'''

# print reverse all items of list abc==cba

# def reverselist(l):
#     rlist=[]
#     for i in l :
#         rlist.append(i[::-1])
#     return rlist
# worfds=['abc','efg','mnpo']
# print(reverselist(worfds))

def total(*x):
    totl=0
    for i in x:
        totl+=i
    return totl
print(total(1,2,3))

