#USING BREAK STATEMENT
# simple program to try the correct pin code 
pin=1234
trials=1
while trials<=3:
    pin_code=int(input("Enter the pin_code>>>"))
    trials+=1
    if pin_code==pin:
        print("CORRECT")
        break
    else:
        print("INCORRECT")
#--------------------------------------------------------------

#USEING CONTINUE STATEMENT 
#simple program to try the correct pin code with continue statement 
pin = 1234
trials = 1
while trials <= 3:
    pin_code = int(input("Enter the pin_code>>> "))
    
    if pin_code != pin:
        print("INCORRECT, try again!")
        trials += 1
        continue

    print("CORRECT")
    break
