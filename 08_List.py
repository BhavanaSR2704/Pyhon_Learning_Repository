#List is a built in data type that stores set of values.It can store elements of different type[int,flot,string,etc]
student=["karan",95.5,19,"Delhi"]
print(student[0])
student[0]="Bhavana"
print(student)

#o/p---------------------->["Bhavana,95.5,19,"Delhi]"


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
items = ["milk", "bread", "eggs", "rice", "apple"]
price = [40, 20, 6, 60, 100] 

item = input("Enter item name: ")

if item in items:
    index = items.index(item)
    cost = price[index]

    print(f"{item} is available.")           #using formatted string

    if cost > 50:
        print(f"Price of {item} is {cost} — It is expensive.")
    else:
        print(f"Price of {item} is {cost} — It is affordable.")

else:
    print(f"{item} is not available in the store.")
