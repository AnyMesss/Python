grade = int(input("Enter your Grade: "))

if grade >= 101:
    print("Please verify your grade again")
    exit()

if (90<= grade <=100):
    print("You got Grade A")
elif (80<= grade <=89):
    print("You got Grade B")
elif (70<= grade <=79):
    print("You got Grade C")
elif (60<= grade <=69):
    print("You got Grade D")
else:
    print("You got Grade F")