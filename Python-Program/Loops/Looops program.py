# a program on the addition of numbers with sequence 1-...

'''x=int(input("enter a num-"))
y=0
total=0
while y<=(x):
    total+=y
    y+=1
print(total)'''

'''x=int(input("enter a num-"))
total=0
y=0
for y in range(x):
   y+=1
   total+=y
print(total)'''

'''x=input("enter a number=")
y=0
total=0
while y<len(x):
    total+=int(x[y])
    y+=1
print(total)'''
'''x=input('enter a num-')
y=0
total=0
while y<len(x):/,for y in range(len(x)):
    total+=int(x[y])
    y+=1
print(total)'''

# print the sum of even numbers between- 1-100 by for loop
'''total=0
y=0
for y in range(0,100,2):/ while y<100:
    y+=2
    total+=y
print(total)'''

#print the each CHARACTERS of the any  words 
'''x="mangal" input("enter a name =")
y=0
while y<len(x):  /for y in range(len(x)):
    print(x[y])
    y+=1'''


#(print a program on find the number of each characters that char how much times come in them words )
    
'''x=input(" Mangal is don ")
y=0
z=""
for y in range(len(x)):
    if x[y] not in z:
      z+=(x[y])
      print(f"{x[y]}={x.count(x[y])}")
      y+=1''' 

'''
x=input("enter anhy words ;-")
z=""
y=0
for y in range(len(x)):
    if x[y] not in z:
        z+=x[y]
        print(f"{x[y]} = {x.count(x[y])}")'''
        


