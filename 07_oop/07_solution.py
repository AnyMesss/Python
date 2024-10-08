#Static method is a method that belongs to a class rather than an instance(Object) of a class
class Car:
    total_car = 0   
    
    def __init__(self, brand, model):
        self.__brand = brand 
        self.model = model
        Car.total_car += 1  
        
    def get_brand(self):
        return self.__brand + " !"
    
    def full_name(self):
        return f"{self.__brand} {self.model}"
    
    def fuel_type(self):
        return "petrol or diesel"
    
    @staticmethod   #is a decorator
    def general_description():
        return "Cars are means of transport"
    
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
        
    def fuel_type(self):
        return "Electric charge"
    
my_car = Car("Tata", "Nexon")
# print(my_car.general_description())
print(Car.general_description())


    
# In Python, static methods are indeed meant to be accessed by the class itself rather than by instances of the class. However, there is a subtle difference in how static methods are defined and accessed in Python compared to other programming languages like Java or C++.

# In Python, static methods are declared using the `@staticmethod` decorator, which specifies that the method should be treated as a static method. However, static methods in Python are not truly bound to the class itself. Instead, they are bound to the class's namespace, which is the same namespace that contains the class's other attributes and methods.

# This means that while static methods can be accessed using the class name, they can also be accessed using an instance of the class, as shown in the example you provided. When you call a static method using an instance of the class, the instance itself is not used in any way. The method is simply called using the class's namespace.

# This behavior is different from static methods in other programming languages, where static methods are truly bound to the class and cannot be accessed using an instance of the class. In Python, the ability to access static methods using both the class name and an instance of the class provides greater flexibility and allows for more concise code in certain situations.

# It's important to note that while static methods can be accessed using both the class name and an instance of the class, they should generally be accessed using the class name for consistency and clarity.

# class MyClass:
#     @staticmethod
#     def my_static_method():
#         print("Hello from static method!")

# # Calling using the class name 
# MyClass.my_static_method()  # Output: Hello from static method!

# # Calling using an object  
# obj = MyClass()
# obj.my_static_method()  # Output: Hello from static method!
