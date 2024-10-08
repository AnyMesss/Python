>>> x = 2
>>> y = 3
>>> z = 4
>>> x+y
5
>>> x + y * z
14
>>> (x + y) * z
20
>>> 40 + 2.23
42.23
>>> int(2.23)
2   
>>> float(40)
40.0
>>> "chai" + "code" 
'chaicode'
>>> "chai" + " code" 
'chai code'
>>> x, y, z
(2, 3, 4)
>>> x + 1, y*2
(3, 6)
>>> y % 2
1   
>>> z ** 2
16  
>>> z ** 5
1024
>>> 100 ** 2
10000
>>> 100 ** 100
100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
>>> 2 ** 100   
1267650600228229401496703205376
>>> 2 ** 1000
10715086071862673209484250490600018105614048117055336074437503883703510511249361224931983788156958581275946729175531468251871452856923140435984577574698574803934567774824230985421074605062371141877954182153046474983581941267398767559165543946077062914571196477686542167660429831652624386837205668069376   
>>> result = 1/3.0
>>> result
0.3333333333333333


>>> repr('chai')
"'chai'"
>>> str('chai')  
'chai'
>>> print('chai') 
chai

repr() provides a string representation suitable for debugging,
str() provides a more user-friendly string representation,
and 
print() is a function for outputting text or values to the console, typically using str() for the conversion.

>>> 1 < 2                                                                
True                                                                     
>>> 5.0 == 5.0                                                           True                                                                     
>>> 4.0 != 5.0
True
>>> x = 2
>>> y = 3
>>> z = 4
>>> x < y < z
True
>>> x < y and y < z 
True

>>> x < y and y < z                                                      
True                                                                     
>>> 1 == 2 < 3                                                           
False                                                                        
>>> 1 == 2 and 2 < 3
False
>> import math                                                          1249
>>> math.floor(3.5)     # gives us closes number below value                                                 9857
3                                                                        7675
>>> math.floor(-3.5)                                                         
-4  
>>> math.trunc(2.8)    # it goes towards zero
2  

# In python Number precisions is almost infinite
>>> 99999999999999999 + 1
100000000000000000
>>> 99999999999999999 * 2.1
2.1e+17
>>> 2 * 200
400 
>>> 2 ** 200 
1606938044258990275541962092341162602522202993782792835301376

>>> 2 + 1j                                                               1249
(2+1j)                                                                   9857
>>> 2 + 1j * 3                                                           7675
(2+3j)                                                                       
>>> (2 + 1j) * 3 
(6+3j)

>>> 0o20                                                                 1249
16                                                                       9857
>>> 0xFF                                                                 7675
255                                                                          
>>> 0b1000
8   
>>> oct(64)
'0o100'
>>> hex(64)
'0x40'
>>> bin(64)
'0b1000000'
>>> int('64',8) 
52  
>>> int('64',16) 
100 
>>> int('10000',2)  
16

>>> x = 1                                                                    
>>> x << 2
4

>>> import random
>>> random.random()
0.2037192321139979
>>> random.random()
0.0010074885127618893
>>> random.random()
0.7793819917167372
>>> random.random()
0.6968627321791954
>>> random.randint(1,10)
3   
>>> random.randint(1,10)
8   
>>> random.randint(1,10)
9   
>>> random.randint(1,10)
7   
>>> random.randint(1,10)
8
>>> random.randint(1,10)
8
>>> random.randint(1,10)
4


>>> l1 = ['lemon','masala','ginger','mint']
>>> random.choice(l1)
'mint'
>>> random.choice(l1)
'mint'
>>> random.choice(l1)
'mint'
>>> random.choice(l1)
'masala'
>>> random.choice(l1)
'ginger'
>>> random.choice(l1)
'mint'
>>> random.choice(l1)
'masala'
>>> random.choice(l1)
'masala'
>>> random.choice(l1)
'lemon'
>>> random.shuffle(l1) 
>>> l1
['mint', 'masala', 'lemon', 'ginger']


>>> 0.1 + 0.1 + 0.4
0.6000000000000001
>>> 0.1 + 0.1 + 0.1
0.30000000000000004
>>> 0.1 + 0.1 + 0.1 - 0.3
5.551115123125783e-17
>>> (0.1 + 0.1 + 0.1) - 0.3 
5.551115123125783e-17
>>> from decimal import Decimal
>>> Decimal('0.1') + Decimal('0.1') + Decimal('0.1')
Decimal('0.3')
>>> Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')
Decimal('0.0')
>>> from fractions import Fraction
>>> myFra = Fraction(2,7)
>>> myFra 
Fraction(2, 7)


>>> setone = {1,2,3,4}
>>> setone & {1,3}    
{1, 3}
>>> setone | {1,3} 
{1, 2, 3, 4}
>>> setone | {1,3,7} 
{1, 2, 3, 4, 7}
>>> setone
{1, 2, 3, 4}
>>> setone - {1,2,3,4} 
set()
>>> type({}) 
<class 'dict'>


>>> type(True)
<class 'bool'>
>>> True == 1
True
>>> False == 0
True
>>> True is 1
<stdin>:1: SyntaxWarning: "is" with 'int' literal. Did you mean "=="?
False
>>> True 
True
>>> True + 4
5   


