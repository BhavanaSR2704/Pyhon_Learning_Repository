#USING BREAK STATEMENT
for i in range(1, 6):
    if i == 3:
        break
    print(i)
#------------------------------------
#USING CONTINUE STATEMENT
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
#~~~~~~~~~~~~~~~~~~USING BOTH ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
pin = 1234

for attempt in range(1, 4):
    pin_code = int(input("Enter the pin_code>>> "))

    if pin_code != pin:
        print("INCORRECT, try again!")
        continue

    print("CORRECT")
    break
else:
    print("Too many wrong attempts. Card blocked!")
#----------------------------------------------------------------
numbers = [10, 15, 0, 20, 25, 30]

for num in numbers:
    if num == 0:
        print("Skipping zero value!")
        continue
    if num % 2 != 0:
        print(num, "is odd")
        continue
    if num == 25:
        print("Found 25, stopping the loop.")
        break
    print(num, "is even")
