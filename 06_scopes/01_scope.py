# username ="AnimeshBiswas"

# def func():
#     # username = "Animesh" 
#     print(username)
    
    
# print(username)
# func() 


x = 99
# def func2(y):
#     z = x + y
#     return z

# result = func2(1)
# print(result)

# def func3():
#     global x     # its used to overwrite the value from the same reference but its not prefer way to do in terms of practise
#     x = 12
    
# func3()
# print(x)


# def f1():
#     x = 88
#     def f2():
#         print(x)
#     return f2  # means return the complete definition of f2 to the f1 but not just definition, but the references to all the variables associated with that definition are also known. This is called bag theory. Is that, you do not just pack a definition along with you, you pack a complete back pack, it has a definition but it also has references of all those memories as to what all you have to take with you.
# myResult = f1() 
# myResult() 

# Below code is exact versions of closure or factory fuctions
def chaicoder(num):  
    def actual(x):
        return x ** num
    return actual


f = chaicoder(2)
# def chaicoder(2):  
#     def actual(x):
#         return x ** 2
#     return actual
print(f(3))
# def chaicoder(2):  
#     def actual(3):
#         return 3 ** 2
#     return actual

g = chaicoder(3)
# def chaicoder(3):  
#     def actual(x):
#         return x ** 3
#     return actual
print(g(3))
# def chaicoder(3):   
#     def actual(3):
#         return 3 ** 3
#     return actual




