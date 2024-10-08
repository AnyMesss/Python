# attribute means variables, instances means create object

class Car:
    total_car = 0
    
    def __init__(self, brand, model):
        self.__brand = brand   # when you put underscores before any variable. It means it has become private now. What I meant by private was that inside the class you will be able to access it but no one. If an object is created then that object is now will no longer be able to access if the object will not be able to access and you want people need to access it somehow. These methodes (get_brand) will have to made
        self.__model = model
        Car.total_car += 1   
    def get_brand(self):
        return self.__brand + ' !'
        
    def full_name(self):
        return f"{self.__brand} {self.__model}"
        
    def fuel_type(self,fuel):
        return f"{fuel}"
    
    @staticmethod
    def general_description():
        return "Cars are means of transport"
    
    @property
    def model(self):
        return self.__model

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
        
    def fuel_type(self):
        return "Electric charge"


my_tesla = ElectricCar("Tesla", "Model S", "85KWH")

# print(isinstance(my_tesla, Car)) 
# print(isinstance(my_tesla, ElectricCar)) 
# print(my_tesla.get_brand())
# print(my_tesla.__brand)

# safari = Car("Tata", "Safari")
# safariOne = Car("Tata", "Safari")
# safariTwo = Car("Tata", "Safari")
# print(safari.fuel_type("disel"))
# print(safari.total_car)
# print(Car.total_car)
# my_car = Car("Tata", "Nexon")
# my_car.model = "City"
# print(my_car.model())
# print(my_car.general_description())
# print(Car.general_description())
    
# my_car = Car("Toyota", "Corolla") # object is created from any class
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())
    
# my_new_car = Car("Tata", "Safari")
# print(my_new_car.brand)
# print(my_new_car.model)

# __init__() it is also called constructor, constructor is method as soon as the object is created from by any class  then this method should be called from the class

class Battery:
    def battery_info(self):
        return "this is battery" 

class Engine:
    def engine_info(self):
        return "This is engine"

class ElectricCarTwo(Battery, Engine, Car):
    pass

my_new_tesla = ElectricCarTwo("Tesla", "Model S")
print(my_new_tesla.engine_info())
print(my_new_tesla.battery_info())