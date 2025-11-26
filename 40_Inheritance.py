# When one class (child/derived)derives the properties and methods of another class(parent/base) is know as the inheritance
class car:
  @staticmethod
  def start():
    print("car started....")
  @staticmethod
  def stop():
    print("car stopped.")
class Toyotacar(car):
  def __init__(self,name):
    self.name=name
car1=Toyotacar("fortuner")
car2=Toyotacar("prices")
print(car1.start())

#------------O/P:-car started....


#Inheritence type
#*Single inheritance
#*Multi-level inhritance
#*Multiple inheritance
