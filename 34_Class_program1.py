

class student:
    def __init__(self,name,marks):   #constructor
        self.name=name     #Attribute
        self.marks=marks     #Attribute
    def display(self):   #method
        print(f"{self.name} scored {self.marks}")
m1=student("Varsha",9)  #object
m2=student("Bhavana",10) #object
m2.display() #calling method      
