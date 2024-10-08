import time
print("chai is here")
username = "Animesh"
print(username)


# >>> f = open('chai.py')
# >>> f.readline()
# 'import time\n'
# >>> f.readline()
# 'print("chai is here")\n'
# >>> f.readline()
# 'username = "Animesh"\n'
# >>> f.readline()
# 'print(username)'
# >>> f.readline()
# ''

>>> f = open('chai.py') 
>>> f.__next__() # this is the core syntax which makes the thing iterated. so if you run it with the paranthesis i.e. () then the o/p will be exactly the same but this is the raw method like the python internally behave and the raw method is not handled properly differnece btw readlines and next is that it will show crash
'import time\n'
>>> f.__next__()
'print("chai is here")\n'
>>> f.__next__()
'username = "Animesh"\n'
>>> f.__next__()
'print(username)'
>>> f.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration


>>> for line in open('chai.py'):
<!-- OR
>>> for line in open('chai.py').readlines(): #optioal to use but it will give extra load to memory
...     print(line) -->
... 
import time

print("chai is here")

username = "Animesh" 

print(username)    



>>> for line in open('chai.py'):
...     print(line, end='')
... 
import time
print("chai is here")
username = "Animesh" 
print(username)



>>> f = open('chai.py')
>>> while True:
...     line = f.readline()
...     if not line: break
...     print(line)
... 
import time

print("chai is here")

username = "Animesh" 

print(username)



>>> test = "Animesh" 
>>> if not test:
...     print('chai')
... 
>>> test            
'Animesh'
>>> test = ""
>>> if not test:
...     print("chai")
... 
chai



>>> mylist = [1,2,3,4] //iterable object
>>> I = iter(myList) 
>>> I
<list_iterator object at 0x0000029A9C559AE0> It is a list iterator pointing the object at this memory location, so we created this list, now you are pointing at the memory location. refer the diagram from the book, what do you get like if you take it as iter object
>>> I.__next__() , then here you have the iter tool, whatever iter tool you are using, whether you are using it or we have used it manually here, then inside it you will get the starting point of the first refernece memory of that object?
1   
>>> I
<list_iterator object at 0x0000029A9C559AE0> now you will see the value inside I is exactly the same, so it is not that your are at that memory reference. when we reach there, the memory reference also keeps changing. All this work is being done internally "next" that i will point to the first one, but internally there is a pointer which i am keeping, it has become the first one, now it is pointing second one. If you go, it is not that the memory reference changes. The list iterator which is from the memory refernece will always point to the starting point
>>> I.__next__()          
2   
>>> I.__next__()
3
>>> I.__next__()
4
>>> I.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration



>>> f = open('chai.py') already done inter(f) by default as compared to in list
>>> iter(f) is f        
True
>>> iter(f) is f.__iter__() 
True


>>> myNewList = [1,2,3] 
>>> iter(myNewList) is myNewList 
False


>>> D = {'a': 1, 'b': 2} 
>>> for key in D.keys():
...     print(key)
... 
a
b
>>> I = iter(D)
>>> I
<dict_keyiterator object at 0x0000029A9C569D00>
>>> next(I)
'a'
>>> next(I)
'b'
>>> next(I)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration


>>> range(5)
range(0, 5)
>>> R = range(5)
>>> R
range(0, 5)
>>> I = iter(R) 
>>> I
<range_iterator object at 0x0000029A9C573E10>
>>> next(I)    
0   
>>> next(I)
1
>>> next(I)
2
>>> next(I)
3
>>> next(I)
4
>>> next(I)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration