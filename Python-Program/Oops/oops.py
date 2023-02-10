# class Person:
#     def __init__(self,fn,ln,age):
#         self.fn= fn
#         self.ln=ln
#         self.age=age 
        
# P1=Person('mangal','don',22)
# p2=Person('shivraj','singh',23)
# print(P1.fn)
# print(p2.age)
# print(P1.ln) 

# class Laptop:
#     def __init__(self,brand,name,price):
#         self.brand=brand
#         self.name=name
#         self.price=price
    
# P1=Laptop("HP",'i25', '20000')
# P2=Laptop('aplle','aplle21',150000)

# print(P1.__List__)

# print(P1.name)
# print(P1.brand)
# print(P2.name)
# print(P2.brand)
# print(P1.price)
                                         # NEW CODE FOR A PROGRAM 
# class Person:
#     def __init__(self,fn,ln,age):
#         self.fn= fn
#         self.ln=ln
#         self.age=age 
#     def full_name(self):
#         return f"{self.fn}{self.ln}"
        
# P1=Person('mangal ','don',22)
# p2=Person('shiv raj',' singh',23)
# print(Person.full_name(P1))
# print(p2.full_name())
# print(P1.fn)
# print(p2.age)
# print(P1.ln) 
                    # NEW CODE FOR A PROGRAM 
# class Laptop:
#     x=25
#     def __init__(self,brand,name,price):
#         self.brand=brand
#         self.name=name
#         self.price=price
        
#     def total_discount(self):
#         discount=self.price*(self.x/100)
#         return self.price-discount
        
# P1=Laptop("HP",'i25', 20000)
# P2=Laptop('aplle','aplle21',150000)
# P2.x=50

# print(P1.__dict__)
# print(Laptop.total_discount(P2))
# print(P2.brand)
# print(P1.total_discount())
                                                 # NEW CODE FOR A PROGRAM 

# class Mobiles:
#     discount=25
#     def __init__(self,brand_name,ram_rom,price,color):
#         self.brand_name=brand_name
#         self.ram_rom=ram_rom
#         self.price=price
#         self.color=color
        
#     def apply_discount(self):
#         x=self.price*(self.discount/100)
#         return self.price-x
    
# M1=Mobiles('apple','4-64',95000,'black')
# M1.discount=30
# M2=Mobiles('vivo','4-64',15000,'silver')
# M2.discount=50
# print(M1.__dict__)
# print(M1.price)
# print(Mobiles.apply_discount(M1))
# print(M2.__dict__)
# print(M2.price)
# print(M2.apply_discount())

                            # AREA OD CIRCLES
                            # INSTANCE METHOD 
                        
# class Circle:
#     count_instance=0
#     pi=3.14
#     def __init__(self,radius):
#         Circle.count_instance+=1
#         self.radius=radius
#     def area(self):
#         return Circle.pi*(self.radius**2)
#         # print(x)
# C1=Circle(3)
# C2=Circle(4)
# print(Circle.count_instance)
# print(C1.area())
# print(Circle.area(C1))
                                # BY CLASS METHOD 

class Person:
    instance_count=0
    def __init__(self,fn,ln,age):
        Person.instance_count+=1
        self.fn= fn
        self.ln=ln
        self.age=age 
           
    #  # CLASS METHOD 
     
    # @classmethod
    # def instance_count(cls):
    #     return f" in this class we used {cls.instance_count} instance /object"
      
                                 # INSTANCE METHOD
                                 
    def full_name(self):           
        return f'{self.fn} {self.ln}'
   
      
P1=Person('mangal','don',22)
p2=Person('shivraj','singh',23)
# print(Person.instance_count)
# print(P1.fn)
# print(p2.age)
# print(P1.ln) 
print(P1.full_name())
# print(Person.instance_count)


class Phone:
    def __init__(self,cost):
        self.pric=cost
        
    def price(self):
        return f"price is 1500 RS  from rate{ self.pric}"
 

class Mobiles(Phone):
    pass

P1=Phone(1500)
M1=Mobiles(25000)
print(type(P1))
print(P1.price())
# print(P1.price())
print(M1.price())