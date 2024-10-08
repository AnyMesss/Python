fruit = "Banana"
color = input("Enter the color of banana: ")

if fruit == "Banana":
    if color == "Green":
        print("Banana is Unripe")
    elif color == "Yellow":
        print("Banana is Ripe")
    elif color == "Brown":
        print("Banana is Overripe")
        exit()