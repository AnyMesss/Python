# def even_generator(limit):
#     li = []
#     for i in range(2, limit + 1, 2):
#         li.append(i)
#     return li
    
# print(even_generator(10))
# PS E:\Python Folder> & C:/Users/Admin/AppData/Local/Microsoft/WindowsApps/python3.12.exe "e:/Python Folder/05_functions/09_solution.py"
# [2, 4, 6, 8, 10]



def even_generator(limit):
    for i in range(2, limit + 1, 2):
        yield i
    
    

for num in even_generator(10):
    print(num)