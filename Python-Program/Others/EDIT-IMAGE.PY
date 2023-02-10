# x=[1,3,2,2]

# # def mylist(list):
#     # a={}
#     # a=[]
# for i in x:
    
#             # if i not in a:
#     print({x.count(i) : x[i]})
#     # i+=1?
#     # print(s)        
#             # a.append(i)
#         # i+=1
#     # return a
# # print(mylist(x))
import os 
os.chdir(r'C:\Program Files')
# x=os.listdir()
x=os.walk(r'C:\Program Files')
# print(x)
for i,j,k in x:
    print(f'current path:{i}')
    print(f'folders name:{j}')
    print(f'files names:{k}')