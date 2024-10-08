>>> chai = "Lemon chai" 
>>> chai
'Lemon chai'
>>> chai = "Masala Chai"  
>>> first_char = chai[0]
>>> print(first_char)
M   
>>> chai
'Masala Chai'
>>> slice_chai = chai[0:6]
>>> print(slice_chai)
Masala
>>> chai[0:6]
'Masala'

>>> num_list = "0123456789"
>>> num_list[:]            
'0123456789'
>>> num_list[3:] 
'3456789'
>>> num_list[:7] 
'0123456'
>>> num_list[0:7:2] # 3rd one is used for hopping the value with -1 of that give value in the 3rd one
'0246'
>>> num_list[0:7:3] 
'036'


>>> chai
'Masala Chai'
>>> print(chai.lower())
masala chai
>>> print(chai.upper()) 
MASALA CHAI
>>> chai   
'Masala Chai'


>>> chai = "   Masala Chai   "
>>> chai
'   Masala Chai   '
>>> print(chai.strip())
Masala Chai


>>> chai = "Lemon Chai" 
>>> print(chai.replace("Lemon","Ginger")) 
Ginger Chai
>>> chai   
'Lemon Chai'
>>> chai = "Lemon, Ginger, Masala, Mint" 
>>> print(chai.split())     
['Lemon,', 'Ginger,', 'Masala,', 'Mint']
>>> print(chai.split(", "))
['Lemon', 'Ginger', 'Masala', 'Mint']


>>> chai = "Masala Chai" 
>>> print(chai.find("Chai")) 
7   
>>> print(chai.find("Chai")) 
7   
>>> print(chai.find("chai"))
-1  
>>> chai = "Masala Chai Chai Chai" 
>>> print(chai.count("Chai")) 
3   


>>> chai_type = "Masala"
>>> quantity = 2
>>> order = "I ordered {} cups of {} chai" 
>>> order
'I ordered {} cups of {} chai'
>>> print(order.format(quantity,chai_type)) 
I ordered 2 cups of Masala chai


>>> chai_variety = ["Lemon", "Masala", "Ginger"] 
>>> chai_variety                                
['Lemon', 'Masala', 'Ginger']
>>> print("".join(chai_variety)) 
LemonMasalaGinger
>>> print(" ".join(chai_variety)) 
Lemon Masala Ginger
>>> print("-".join(chai_variety)) 
Lemon-Masala-Ginger
>>> print(", ".join(chai_variety)) 
Lemon, Masala, Ginger


>>> chai
'Masala Chai Chai Chai'
>>> chai = "Masala Chai" 
>>> print(len(chai)) 
11  
>>> chai
'Masala Chai'
>>> for letter in chai:
...     print(letter)
... 
M   
a   
s   
a   
l   
a   
    
C   
h   
a   
i   


>>> chai = "He said, \"Masala chai is awesome\" "  # Do not want to treat qoute as a string then use "\" before doube qoute at a beginning and end
>>> chai
'He said, "Masala chai is awesome" '


>>> chai = "Masala\nChai" 
>>> chai
'Masala\nChai'
>>> print(chai)
Masala
Chai  
>>> chai = r"Masala\nChai" 
>>> print(chai)
Masala\nChai


>>> chai = r"c:\user\pwd\"  # if you want raw data/object use "r"
  File "<stdin>", line 1
    chai = r"c:\user\pwd\"
           ^
SyntaxError: unterminated string literal (detected at line 1)
>>> chai = r"c:\user\pwd"  
>>> print(chai)
c:\user\pwd
>>> chai = "c:\user\pwd"  
  File "<stdin>", line 1
    chai = "c:\user\pwd"
           ^^^^^^^^^^^^^
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \uXXXX escape
>>> chai = "c:\\user\\pwd" 
>>> print(chai)
c:\user\pwd


>>> chai
'c:\\user\\pwd'
>>> chai = "Masala Chai"
>>> print("Masala" in chai) 
True
>>> print("Masalaa" in chai) 
False