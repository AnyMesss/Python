# def print_kwargs(name, power):
#     print("Name ", name, " Power: ", power)


# print_kwargs(name="Animesh", power="laser")
# print_kwargs(power="laser", name="Animesh")
# print_kwargs(name="Animesh")
# print_kwargs(name="Animesh", power="laser", enemy = "Dr. Jackaal")
# PS E:\Python Folder> & C:/Users/Admin/AppData/Local/Microsoft/WindowsApps/python3.12.exe "e:/Python Folder/05_functions/08_solution.py"
# Name  Animesh  Power:  laser
# Name  Animesh  Power:  laser
# Traceback (most recent call last):
#   File "e:\Python Folder\05_functions\08_solution.py", line 7, in <module>
#     print_kwargs(name="Animesh")
# TypeError: print_kwargs() missing 1 required positional argument: 'power'




# def print_kwargs(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")


# print_kwargs(name="Animesh", power="laser")
# print_kwargs(power="laser", name="Animesh")
# print_kwargs(name="Animesh")
# print_kwargs(name="Animesh", power="laser", enemy = "Dr. Jackaal")
# PS E:\Python Folder> & C:/Users/Admin/AppData/Local/Microsoft/WindowsApps/python3.12.exe "e:/Python Folder/05_functions/08_solution.py"
# name: Animesh
# power: laser
# power: laser
# name: Animesh
# name: Animesh
# name: Animesh
# power: laser
# enemy: Dr. Jackaal


def print_kwargs(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    
    
print_kwargs(name="Animesh", power="Laser")
print_kwargs(name="Animesh")
print_kwargs(name="Animesh", power="Laser", enemy = "Mera chacha")