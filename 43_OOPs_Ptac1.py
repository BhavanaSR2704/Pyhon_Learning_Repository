from abc import ABC, abstractmethod

# ---------- Abstraction ----------
class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

    def sleep(self):
        print("Animal is sleeping...")


# ---------- Inheritance + Encapsulation ----------
class Dog(Animal):
    def __init__(self):
        # Encapsulated variable (private)
        self.__name = None

    # Getter and Setter for Encapsulation
    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    # ---------- Polymorphism (Overriding) ----------
    def sound(self):
        print("Dog barks: Woof Woof!")

    # ---------- Polymorphism (Method Overloading in Python Way) ----------
    def eat(self, food=None):
        if food is None:
            print("Dog is eating...")
        else:
            print(f"Dog is eating {food}...")


# ---------- Main Code ----------
d = Dog()

# Encapsulation
d.set_name("Rocky")
print("Dog Name:", d.get_name())

# Inheritance + Abstraction
d.sound()     # overridden method
d.sleep()     # method from abstract class

# Polymorphism (Overloading-like behavior)
d.eat()
d.eat("bones")

