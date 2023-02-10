# x=['a','b','c', 'd']
# y=[5,6,7,8   ]
# print(dict(zip(x,y)))

# x=[(1,2),(3,4),(5,6),(7,8),(9,0)]
# l1,l2=list(zip(*x))
# print(l1)
# print(l2)

# avg=lambda *args : [(sum(pair)/len(pair)) for pair in zip(*args)]
# x=[1,2,3]
# y=[4,3,2]
# print(avg(x,y))

# def avg_finder(l1,l2):
#     average=[]
#     for i in zip(l1,l2):
#         average.append(sum(i)/len(i))
#     return average
# x=[1,2,3,4]
# y=[7,6,5,8]
# print(avg_finder(x,y))

# def avg_finder(*args):
#     avg=[]
#     for i in zip(*args):
#         avg.append(sum(i)/len(i))
#     return avg
# x=[1,2,3,4]
# y=[7,6,5,8]
# z=[2,3,4,1]
# print(avg_finder(x,y,z))

class Person:
    def __init__(self,first,last,age):
        self.first_name=first
        self.last_name=last
        self.age=age
    
    def full_name(self):
        if self.age>18:
            print(self.first_name,self.last_name,self.age)
        return f"{self.first_name} {self.last_name}"
    
class student(Person):
    def __init__(self,first,last,age,father_name,mother_name):
        Person.__init__(self,first,last,age)
        # super().__init__(self,first,last,age)
        self.father_name=father_name
        self.mother_name=mother_name
        
P1=Person('Mangal', 'Don', 12 )
S2=student( 'shiv','raj',20,'bhoop singh','geeta devi')
# print(S2.father_name)
# pP1.full_name()
S2.full_name()


    

# def avg_finder(*args):
#     avg=[]
#     for i in zip(args):
#         avg.append(sum(i) /len(i))
#     return avg 

# print(avg_finder(x,y))