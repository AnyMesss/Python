class Car:
    total_car = 0    #initialise the variable
    
    def __init__(self, brand, model):
        self.__brand = brand 
        self.model = model
        Car.total_car += 1  # or self.total_car += 1
        
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
    
safari = Car("Tata", "Safari")
safariTwo = Car("Tata", "Nexon")
safariThree = Car("Tata", "Safari")
# print(safari.fuel_type())
print(safari.total_car)
