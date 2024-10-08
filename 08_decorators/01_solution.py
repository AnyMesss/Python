# Decorators is the concept of tollbooth, As soon as you come to the tollbooth  on the road, it is decided there that if there will be a car. so they will pay this much and if it is a bus then there will be these charges and so on it depends on which vehicles you taking to the tollboot and pay according to that but to pass through will have to be toll booth
#We take a function and pass it out through a box or we pass it on through a pipe, then if we have to do some extra work on it, we do it, otherwise we do it as it is.

# import time

# def timer(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         print(start)
#         result = func(*args, **kwargs) <- Function will be executed and it will be stored in the result variable
#         end = time.time()
#         print(end)
#         print(f"{func.__name__} ran in {end-start} time")
#         return result
#     return wrapper
# we have created a timer function, we have created a wrapper inside it,because by executing it inside the wrapper, and then return the wrapper, then what did we do? we had this result, so here we made a function and this returned the 'result' and finally  we returned the wrapper
# @timer  #<----- as soon as you put the timer here, then this is one of the best super powers of python to create a decorator, the syntax is also very clean and here. you just write above. if you have written @timer above any function, now what will happen actually, whenever you call this function, example_function(), then this function will not be called directly. This function will pass through the "timer" only or whatever new name you have given it. 
# def example_function(n):
#     time.sleep(n)        #system goes sleep for that period of time
    
# example_function(5)

# Decorator in a nutshell
# Create a method in it, inside we create a method usually and inside it we put whatever function we have passed from here and get it executed and finally we wrap it here
#OR
#Create a function inside a function and our function is executed inside it

