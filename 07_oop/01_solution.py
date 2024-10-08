# attribute means variables, instances means create a object or a object

class Car:
    def __init__(self, brand, model): # __init__() it is also called constructor, constructor is method as soon as the object is created from by any class  then this method should be called from the class
        self.brand = brand
        self.model = model
        
    
my_car = Car("Toyota", "Corolla") #making object from the class
print(my_car.brand)
print(my_car.model)

my_new_car = Car("Tata", "Safari")
print(my_new_car.model)
print(my_new_car.brand)
    