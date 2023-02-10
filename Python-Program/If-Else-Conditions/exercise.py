# ask the name from user and print count of each words /

x=input("enter your name ")
i=0
while i<len(x):
    print(f"{x[i]}:{x.count(x[i])}")
    i+=1

'''x=input("enter a name :")
i=0
y=""
while i<len(x):
    if x[i] not in y:
        y+=x[i]
        print(f"{x[i]}={x.count(x[i])}")
    i+=1'''

# x=input("enter your name ")[::-1]
# i=0
# y=""
# while i<len(x):
#     if x[i] not in y:
#         y+=x[i]
#         print(f"{x[i]}={x.count(x[i])}")
#     i+=1

# x=input("enter the value :- ")
# print(x)
x=input("enter your name")[::-1]
i=0
y=""
while i<len(x):
 if x[i] not in y:
    y+=x[i]
    print(f"{x[i]}={x.count(x[i])}")
    i+=1