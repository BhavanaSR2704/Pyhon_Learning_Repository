# Hiding the implementation details of a class and only showing the essential features to the user 
class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("Car started...")

# creating objects
car1 = Car()
car2 = Car()

# calling start() for car2
car2.start()

#----------------------------O/P
#Car started...
