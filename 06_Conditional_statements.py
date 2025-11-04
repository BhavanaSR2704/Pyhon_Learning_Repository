#SYNTAX
# if condition:
    # code to execute if condition is True

# elif another_condition:
    # code to execute if the above condition is False
    # and this condition is True

# else:
    # code to execute if all above conditions are False
signal=input("Enter the colour of signal:\n")
if signal=="RED":
    print("STOP")
elif signal=="YELLO":
    print("READY")
elif signal=="GREEN":
    print("GO")
else:
    print("PLEASE ENTER THE SIGNAL COLOURS ONLY , WITH CAPITAL LETTERS")
