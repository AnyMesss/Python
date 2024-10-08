# global_var = "I am a global variable"

# def outer_function():
#     enclosing_var = "I am a enclosing variable"
    
#     def inner_function():
#         local_var = "I am a local variable"
#         print(local_var)
#         print(enclosing_var)
#         print(global_var)
        
#     inner_function()
#     # print(local_var) -> outer function cant access inner function variable
    
# outer_function()


# Closure Example

# def outer_function(msg):
#     def inner_function():
#         print(f"Message: {msg}")
#     return inner_function

# closure_function = outer_function("Hello, World!")
# closure_function()

def multiplier(factor):
    def multiply_by(x):
        return x * factor
    return multiply_by

times_two = multiplier(2)
print(times_two(3))