# with open("MYFILE.txt","w") as wf:
#     wf.write(""" its new file created by mangal 22 
#         its a grat file for print 
#         mangal is don
#         whats are you saying 
#         its a new type of function for file handling """)
#     wf.close()
# with open("MYFILE.txt",'r') as rf:
#     for i in rf:
#         print(i ,end='')
# # print(f.read(4))
# # print(f.readline())
# import pdb
# pdb.set_trace()
# with open('MYFILE.txt','r') as rf:
#     with open('NEW__FILE.txt','a') as wf:
#         for line in rf.readlines():
#             # wf.write(i)
#             x,y=line.split('=')
#             wf.write(f"{x} has salery is {y}")

x=input("enter your name--")[::-1]
print(x)

