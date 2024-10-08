input_str = "Python"
reversed_str = ""

for char in input_str:
    print(char)                     # dry run
    reversed_str = char + reversed_str
    print(reversed_str)             # dry run
    
print(reversed_str)