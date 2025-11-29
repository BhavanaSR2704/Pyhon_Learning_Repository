num=int(input("Enter the number:"))
match num:
    case n if n >0:
        print("positive number")
    case n if n < 0:
        print("Negative number")
    case _:                             #It's like else statement
        print("It's zero")
