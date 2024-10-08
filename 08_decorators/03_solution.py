import time

def cache(func):
    cache_value = {}  # the main reasons it uses dictionary because it is very easy to access things in a dictionary, when can also use arrays, but what is in the array then you have to keep indexing etc., then take care of indexing of everything it is not possible. So, what we will actually do is, whatever we will do on the "args" here, we will make a key out of it then, whenever we have to access the value on the basis of key
    print(cache_value) 
    def wrapper(*args): 
        if args in cache_value:
            return cache_value[args] 
        result = func(*args)
        cache_value[args] = result
        return result
    return wrapper

@cache
def long_running_function(a, b):
    time.sleep(4)
    return a + b

print(long_running_function(2, 3))

print(long_running_function(2, 3))

print(long_running_function(4, 3))

# boilerplate decorator

# import time

# def cache(func):
#     cache_value = {}  
#     def wrapper(*args):
#         result = func(*args)
#         return result
#     return wrapper


# def long_running_function(a, b):
#     time.sleep(4)
#     return a + b