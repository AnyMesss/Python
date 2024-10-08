>>> tea_varities = ["Black","Green", "Oolong", "White"]  
>>> tea_varities
['Black', 'Green', 'Oolong', 'White']
>>> print(tea_varities) 
['Black', 'Green', 'Oolong', 'White']
>>> print(tea_varities[0]) 
Black
>>> print(tea_varities[1]) 
Green
>>> print(tea_varities[-1]) 
White
>>> print(tea_varities[1:3]) 
['Green', 'Oolong']
>>> print(tea_varities[:3])  
['Black', 'Green', 'Oolong']
>>> print(tea_varities[2:]) 
['Oolong', 'White']
>>> print(tea_varities[:3:2]) 
['Black', 'Oolong']
>>> tea_varities[3] = "Herbal" 
>>> print(tea_varities)
['Black', 'Green', 'Oolong', 'Herbal']
>>> print(tea_varities[1:2])   
['Green']
>>> tea_varities[1:2] = "Lemon" 
>>> tea_varities               
['Black', 'L', 'e', 'm', 'o', 'n', 'Oolong', 'Herbal']
>>> tea_varities[1:5] = ["Green"]
>>> tea_varities                 
['Black', 'Green', 'n', 'Oolong', 'Herbal']
>>> tea_varities[1:3] = ["Green"] 
>>> tea_varities
['Black', 'Green', 'Oolong', 'Herbal']
>>> tea_varities[1:3]            
['Green', 'Oolong']
>>> tea_varities[1:3] = ["Lemon", "Masala"] 
>>> tea_varities     
['Black', 'Lemon', 'Masala', 'Herbal']

>>> tea_varities[1:1]
[]  
>>> tea_varities[1:1] = ["test", "test"] 
>>> tea_varities     
['Black', 'test', 'test', 'Lemon', 'Masala', 'Herbal']
>>> tea_varities[1:2]
['test']
>>> tea_varities[1:3] 
['test', 'test']
>>> tea_varities[1:3] = []
>>> tea_varities      

>>> tea_varities     
['Black', 'Lemon', 'Masala', 'Herbal']
>>> for tea in tea_varities:
...     print(tea)
... 
... 
Black 
Lemon 
Masala
Herbal
>>> for tea in tea_varities:
...     print(tea, end="-")
... 
Black-Lemon-Masala-Herbal->>> 


>>> if "Oolong" in tea_varities:
...     print("I have Oolong tea")
... 
>>> tea_varities.append("Oolong") #append functions is used to add the value at the last positions
>>> if "Oolong" in tea_varities:
...     print("I have Oolong tea")
... 
I have Oolong tea


>>> tea_varities
['Black', 'Lemon', 'Masala', 'Herbal', 'Oolong']
>>> tea_varities.pop()
'Oolong'
>>> tea_varities       
['Black', 'Lemon', 'Masala', 'Herbal']
>>> tea_varities.remove("Lemon")
>>> tea_varities 
['Black', 'Masala', 'Herbal']
>>> tea_varities.insert(1, "green")
>>> tea_varities                   
['Black', 'green', 'Masala', 'Herbal']

>>> tea_varities_copy = tea_varities.copy() # to create a separate object in memory  then use copy functions then after both refereces will not share same object instead it will create separate object and use them according to that
>>> tea_varities_copy                      
['Black', 'green', 'Masala', 'Herbal']
>>> tea_varities_copy.append("Lemon") 
>>> tea_varities_copy                
['Black', 'green', 'Masala', 'Herbal', 'Lemon']


>>> range(10) # range is exclusive i.e n-1
range(0, 10)
>>> print(range(10)) 
range(0, 10)
>>> y = range(10)
>>> y
range(0, 10)
>>> squared_nums = [x**2 for x in range(10)] 
>>> squared_nums                            
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> cube_num = [y**3 for y in range(10)] 
>>> cube_num                            
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
