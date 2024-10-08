# def sum_all(*args):
#     print(args)
#     for i in args:
#         print(i * 2)
#     return sum(args)
    
# print(sum_all(1,2,3))
# print(sum_all(1,2,3,4,5))
# print(sum_all(1,2,3,4,5,6,7,8))


# def sum_all(*chai): its prefer to write in args not any name as a good practise pov
#     return sum(chai)
    
# print(sum_all(1,2))
# print(sum_all(1,2,3,4,5))
# print(sum_all(1,2,3,4,5,6,7,8))
# PS E:\Python Folder> & C:/Users/Admin/AppData/Local/Microsoft/WindowsApps/python3.12.exe "e:/Python Folder/05_functions/07_solution.py"
# 3
# 15
# 36


# def sum_all(*args):
#     print(*args)
#     return sum(args)
    
# print(sum_all(1,2))
# print(sum_all(1,2,3,4,5))
# print(sum_all(1,2,3,4,5,6,7,8))
# PS E:\Python Folder> & C:/Users/Admin/AppData/Local/Microsoft/WindowsApps/python3.12.exe "e:/Python Folder/05_functions/07_solution.py"
# 1 2
# 3
# 1 2 3 4 5
# 15
# 1 2 3 4 5 6 7 8
# 36


# def sum_all(*args):
#     print(args)
#     return sum(args)
    
# print(sum_all(1,2))
# print(sum_all(1,2,3,4,5))
# print(sum_all(1,2,3,4,5,6,7,8))
# PS E:\Python Folder> & C:/Users/Admin/AppData/Local/Microsoft/WindowsApps/python3.12.exe "e:/Python Folder/05_functions/07_solution.py"
# (1, 2)
# 3
# (1, 2, 3, 4, 5)
# 15
# (1, 2, 3, 4, 5, 6, 7, 8)
# 36


def even_generator(limit):
    for i in range(2, limit + 1, 2):
        yield i
        
for num in even_generator(10):
    print(num)