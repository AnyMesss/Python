# what it actually means polymorphism is the word morphis meaning how many can take form and poly means many forms which can hold. e.g. plus(+) add decimal, numbers, strings
class Car:
    def __init__(self, brand, model):
        self.__brand = brand 
        self.model = model
        
    def get_brand(self):
        return self.__brand + " !"
    
    def full_name(self):
        return f"{self.__brand} {self.model}"
    
    def fuel_type(self):
        return "petrol or diesel"
    
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
        
    def fuel_type(self):
        return "Electric charge"
    
my_tesla = ElectricCar("Tesla", "Model S", "85KWH")
print(my_tesla.fuel_type())

safari = Car("Tata", "Safari")
print(safari.fuel_type())

