password = "Secure3P@ss"
password_length = len(password)

if password_length < 6:
    strenght = "weak"
elif password_length < 10:
    strenght = "Medium"
else:
    strenght = "Strong"
    
print("Password strength is: ", strenght)