age = int(input("Provide me an age: "))
day = "Wednesday"

# price = 12 if age >= 18 else 8 
# or
if age >= 18:
    Price = 12
else:
    Price = 8
    
if day == "Wednesday":
    # Price = Price - 2
    Price -= 2
    
print("Ticket price for you is $", Price)