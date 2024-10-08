pet = input("Enter Pet Type: ")
age = int(input("Enter Pet age: "))

if pet == "Dog":
    if age < 2:
        print("Puppy Food")
    else:
        print("Adult Food")
elif pet == "Cat":
    if age > 5:
        print("Senior Food")
    else:
        print("Babby Food")
else: 
    print("Sorry This Pet Is Not Defind")