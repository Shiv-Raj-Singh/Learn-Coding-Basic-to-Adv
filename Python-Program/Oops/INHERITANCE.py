# class Mobiles :
#     def __init__(self,brand,model,price):
#         self.brand=brand
#         self.model=model
#         self.price=price 
#     def fn(self):
#         return f"{self.brand}{self.model}"   
    
    
# class New_Mobiles(Mobiles):
#     def __init__(self,brand,model,price,ram_rom,camera):
#         # Mobiles.__init__(self,brand,model,price)
#         super().__init__(brand,model,price)
#         self.ram_rom=ram_rom
#         self.camera=camera

# M1=Mobiles('NOKIA',"  1100",1800 )
# M2=New_Mobiles('vivo','  v7+',18000,'4--64'  ,'64 mega' )

# print(M1.__dict__)
# print(Mobiles.fn(M1))
# print(New_Mobiles.fn(M2))

# print(M1.price)
# print(M2.__dict__)
# print(M2.price)

class Mobiles:
    discount=0
    def __init__(self,brand_name,price):
        self.brand_name=brand_name
        self.price=price    
    def apply_discount(self):
        x=self.price*(self.discount/100)
        return self.price-x
    def full_name(self):
        return f'{self.brand_name} is a simple mobile its cost is  {self.price}'

class New_Mobiles(Mobiles):
    def __init__(self,brand_name,ram_rom,price,color):
        super().__init__(brand_name,price)
        self.color=color
        self.ram_rom=ram_rom
    def full_name(self):
        return f" {self.brand_name}  {self.color} can we purchase in {self.price} its ram-rom is {self.ram_rom}"
    def apply_discount(self):
        x=self.price*(self.discount/100)
        return self.price-x
    
class a_Mobiles(New_Mobiles):
    def __init__(self,brand_name,ram_rom,price,color,camera):
        super().__init__(brand_name,price,ram_rom,color)
        self.camera=camera
    def full_name(self):
        return f" {self.brand_name}  {self.color} can we purchase in {self.price} its ram-rom is {self.ram_rom} and camera {self.camera} also"
    def apply_discount(self):
        x=self.price*(self.discount/100)
        return self.price-x
    
Mobiles.discount=10 
New_Mobiles.discount=20
a_Mobiles.discount=35
       
M1=Mobiles('Samsung',1500)
N_M1=New_Mobiles('VIVO','4-64', 14000 ,'black')
A_M1=a_Mobiles('apple','4-64',95000,'black','64 MP')

print(M1.full_name())
print(M1.__dict__)
print(M1.price)
print(M1.apply_discount())
print(N_M1.__dict__)
print(N_M1.full_name()) 
print(N_M1.price)
print(N_M1.apply_discount())
print(A_M1.__dict__)
print(A_M1.full_name())
print(A_M1.price)
# print(help(A_M1))

