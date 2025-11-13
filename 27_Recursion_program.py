#Counting down ATM cash dispensing using recursion
def dispense_cash(amount):
    if amount == 0:
        print("All cash dispensed")
        return
    else:
        print("Dispensing ₹100 note")
        dispense_cash(amount - 100)  # recursive call

amount = int(input("Enter amount (in multiples of 100): "))
dispense_cash(amount)

#--------------------------------------------------------
#OUT PUT
Enter amount (in multiples of 100): 500
Dispensing ₹100 note
Dispensing ₹100 note
Dispensing ₹100 note
Dispensing ₹100 note
Dispensing ₹100 note
All cash dispensed
