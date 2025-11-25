# Used to delet the object properties or object itself
#del s1.name
#del s1
class Laptop:
    def __init__(self, brand, ram):
        self.brand = brand
        self.ram = ram

    def show(self):
        print("Brand:", self.brand)
        print("RAM:", self.ram)


# Creating object
l1 = Laptop("DELL", "16GB")

l1.show()   # printing details

# deleting object
del l1

# Now if we try to print
# print(l1)   # This will give error because l1 is deleted
