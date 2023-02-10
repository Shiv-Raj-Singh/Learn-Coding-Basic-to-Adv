'''x=int(input("enter a number "))
total=0
for i in range(1,1+x):
    total+=i
    print("total")'''

# the sum of 1-20 numbers with sequence ,
'''x=0
y=1
while y<=20:
    x=x+y
    y=y+1
    print(f"x={y}")'''

# the sum of 1-20 numbers with squence by using for loop 
'''y=int(input("enter a numbar"))
x=0
for i in range(1,y+1):
    x+=i
print(f"x={i}")'''
# x=(input("enter a number "))
'''y=0
total=0
while y<len(x):
    total+=int(x[y])
    y+=1
print(total)er a number ")
for y in range(0,len(x)):
    i+=int(x[y])
print(i)'''
'''i=0
x=input("ent'''

'''x=input("enter a name ")[::-1]
y=0
z=""
while y<len(x):
    if x[y] not in z: 
       z+=x[y]
    print(f"{x[y]}={x.count(x[y])}")
    y+=1'''

x=input("enter a name ")
y=""
for z  in range(x):
    if x[z] not in y:
        print(f"{x[z]}-{x.count(x[z)}}")
        y+=x[z]