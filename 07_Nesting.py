#Nested if means an if statement written inside another if block.
#SYNTAX
#if condition1:
    # code
    #if condition2:
        # nested code
    #else:
        # nested else block
#elif condition3:
    # code for elif
#else:
    # final else block
age = 20
citizen = "Indian"

if age >= 18:
    if citizen == "Indian":
        print("Eligible to vote in India")
    else:
        print("Not eligible — citizenship required")
else:
    print("Not eligible — age must be 18 or above")


