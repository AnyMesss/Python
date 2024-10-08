# Tuple is opposite of list i.e. tuple is immutable
>>> tea_types = ("Black","Green","Oolong")
>>> tea_types                             
('Black', 'Green', 'Oolong')
>>> tea_types[0]
'Black'
>>> tea_types[-1] 
'Oolong'
>>> tea_types[1:] 
('Green', 'Oolong')
>>> tea_types[0] = "Lemon" 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignmentz

>>> len(tea_types)
3   
>>> more_tea = ("Herbal","Earl Grey") 
>>> all_tea = more_tea + tea_types
>>> all_tea
('Herbal', 'Earl Grey', 'Black', 'Green', 'Oolong')
>>> if "Green" in all_tea:
...     print("I have green tea")
... 
I have green tea
>>> more_tea = ("Herbal","Earl Grey","Herbal") 
>>> more_tea
('Herbal', 'Earl Grey', 'Herbal')
>>> more_tea.count("Herb") 
0

>>> tea_types
('Black', 'Green', 'Oolong') # many times you get returns from the database like this one and this is a very common thing to return from the database and it happens many times. you can use tuples, unwrapping the tuple
>>> (black,green, Oolong) = tea_types # in this conditions length should be same on RHS AND LHS 
>>> black
'Black'
>>> type(tea_types)
<class 'tuple'>