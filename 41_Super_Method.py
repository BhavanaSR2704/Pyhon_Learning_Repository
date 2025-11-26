# super() method is used to acces methods of the parent class
class car :
  def __init__(self,type):
    self.type=type
  @staticmethod
  def start():
    print("car start..")
  @staticmethod
  def stop():
    print("car stopped.")
class Toyotacar(car):
  def __init__(self,name,type):
    super().__init__(type)
    self.name=name
    super().start()
car1=Toyotacar("prices","electic")
print(car1.type)

#------------O/P:-car start..
                  #electic
