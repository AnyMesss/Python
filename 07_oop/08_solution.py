class Car:
    total_car = 0   
    
    def __init__(self, brand, model):
        self.__brand = brand 
        self.__model = model  #when you use undersocres you cant able to overwrite the value and access directly
        Car.total_car += 1  
        
    def get_brand(self):
        return self.__brand + " !"
    
    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self):
        return "petrol or diesel"
    
    @staticmethod   #is a decorator
    def general_description():
        return "Cars are means of transport"
    
    @property #when you use property decorator the first thing you do is intentionally is you want to hide it the property that nobody will access it and if anyone want to access then only through this method 
    def model(self):
        return self.__model
    
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
        
    def fuel_type(self):
        return "Electric charge"
    
my_car = Car("Tata", "Nexon")
# my_car.model = "City"

# print(my_car.model()) # when you access the method it gives error and gives rights to access as property not method
print(my_car.model) 

