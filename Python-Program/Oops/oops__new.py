# class Vehicles:
#     color='white'   
#     def __init__(self,name,max_speed,mileage,capacity):
#         self.name=name
#         self.max_speed=max_speed
#         self.mileage=mileage
#         self.capacity=capacity
        
#     def total_fare(self):
#         x=self.capacity*100
#         return f"total fare is {x} and one person fare is {x/self.capacity}"

# class Bus(Vehicles):
#     def total_fare(self):
#         super().total_fare()
#         total_fare_bus=self.capacity*100
#         maintenance_charge=(total_fare_bus*10)/100
#         final_amount=total_fare_bus+maintenance_charge
#         # return (final_amount)
#         print(f"total fare is {final_amount} and one person fare is {final_amount/self.capacity}")
# class Car(Vehicles):
#     pass
    # def __init__(self,name,max_speed,mileage,capacity):
    #     Vehicles.__init__(self,name,max_speed,mileage)
    #     self.capacity=capacity
        
    # def seating_cap(self):
    #     return f" the capacity of {self.name} for seating are {self.capacity} peoples "
    
#         # return super().seating_cap(self.capacity)
# V1=Vehicles('ven',90,30,8)
# B1=Bus('school bus',150,15 ,50 )
# print(V1.__dict__)
# print(V1.total_fare())
# print(B1.__dict__)
# print(B1.total_fare())
# print(B1.color)

class Rjit_Hostel:
    def __init__(self,first,second,third,final):
        self.first_year=first
        self.second_year=second
        self.third_year=third
        self.finaal_year=final
        
    
    def total(self):
        total_students= self.finaal_year + self.first_year + self.second_year + self.third_year
        return f"{self.finaal_year} total students of final year in hostel there total students are {total_students}"
    
    def lateral_entry(self):
        
        
        x=(self.second_year*10)/100
        lateral=self.second_year-x
        return lateral
    
class Rjit(Rjit_Hostel):
    def __init__(self,first,second,third,final,m_first,msecond):
        super.__init__(self,first,second,third,final)
        self.m_teck_first_year=m_first
        self.m_teck_second_year=msecond
    def lateral_entry(self):
        total_lateral_entry=self.second_year + (self.second_year*20)/100
        return total_lateral_entry
    def total(self):
        super().total()
        x= self.finaal_year+self.first_year+self.second_year+self.third_year +self.m_teck_first_year + self.m_teck_second_year
        return f"{x} total students of rjit in which lteral entry in rjit there total students are {self.second_year} "

        
        
# RJ1=Rjit_Hostel( 132,76,56,35)

# print(RJ1.__dict__)
# print(RJ1.total())
# print(RJ1.lateral_entry())
R=Rjit(120,80,75,38)
print(R.__dict__)
print(R.total())
print(R.lateral_entry())
