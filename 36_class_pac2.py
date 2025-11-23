#Static Methods
#Method that not uses the self parameter 
class Student :
  @staticmethod 
  def college():
    print("ABC College")

#----------------------------------------------------------------------------
#Decorators allow us to wrap another function in order to extend the behaviour of the wrapped functions without permanently modifying it
def hello():
  print("hello")
@staticmethod
s1.hello()

#---------O/P :- hello
