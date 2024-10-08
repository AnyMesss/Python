class Car:
    def __init__(self, brand, model):
        self.__brand = brand # when you put underscores before any variable/attribute. It means that it has become private now. What I meant by private is that inside the class you will be able to access it but the object will not able to access it. If an object is created then that object is now will no longer be able to access and you want people need to access it somehow. These methodes (get_brand) will be made availabe to access
        self.model = model
        
    def get_brand(self):
        return self.__brand + " !"
    
    def full_name(self):
        return f"{self.__brand} {self.model}"
    
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    
my_tesla = ElectricCar("Tesla", "Model S", "85KWH")
# print(my_tesla.brand) # since attribute is made private then the object no longer have the right to access  
print(my_tesla.get_brand())  

#study setter