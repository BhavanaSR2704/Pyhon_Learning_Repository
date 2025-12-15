password = input("Enter a password: ")

strength = 0

if len(password) >= 8:
    strength += 1
if any(char.isdigit() for char in password):
    strength += 1
if any(char.isupper() for char in password):
    strength += 1
if any(char.islower() for char in password):
    strength += 1
if any(char in "!@#$%^&*" for char in password):
    strength += 1

if strength <= 2:
    print("Weak Password")
elif strength == 3:
    print("Medium Password")
else:
    print("Strong Password")

