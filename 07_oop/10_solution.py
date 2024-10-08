class Car:
    total_car = 0   
    
    def __init__(self, brand, model):
        self.__brand = brand 
        self.__model = model  
        Car.total_car += 1  
        
    def get_brand(self):
        return self.__brand + " !"
    
    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self):
        return "petrol or diesel"
    
    @staticmethod  
    def general_description():
        return "Cars are means of transport"
    
    @property 
    def model(self):
        return self.__model
    
    


class Battery:
    def battery_info(self):
        return "This is Battery"
class Engine:
    def engine_info(self):
        return "This is engine"
    
class ElectricCarTwo(Battery, Engine, Car):
    pass

my_new_tesla = ElectricCarTwo("Tesla", "Model S")
print(my_new_tesla.engine_info())
print(my_new_tesla.battery_info())