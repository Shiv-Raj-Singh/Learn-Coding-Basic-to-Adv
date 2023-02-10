# l=['abc', 'mangal','rajugujjjarji']

# a=list(map(len,l))          #( #using map function)  
# for i in l:
#     print(i)
#     print(len(i))

# for i,pos in enumerate(l):   # (using enumerate for print indx also )
#     print(f"{i}----{pos}")
    
# def func(l,**kwargs):
#     if kwargs.get("strg"==True):
#         return [i[::-1].title() for i in l]
#     else:
#         return{i.title() for i in l}
# x=['abc', 'mangal','rajugujjjarji']
# # print(func(x))
# print(func(x,"strg"==True ))

# x=[1,2,3,4]
# gy=[]
# for i in x:
#     gy.append(i**2)
#     return gy


# x=[1,2,3,4]
# y=list(map(lambda a:a**2,x))
# print(y)

from json import decoder


x=[1,2,3,4,5]
# y=0
# for i in x:
#     print(f" on {y} position {i} ")
#     y+=1
 
for i,y in enumerate(x):
    print(f"{y} position {i} ")
    

    
