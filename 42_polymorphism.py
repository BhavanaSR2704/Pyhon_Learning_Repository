# OPERATOR OVERLOADING
#when the same operator is allowed to have different meaning according to the context
#For example 
# a+b# addition------------------>a.__add__(b)

class complex:
  def __init__(self,real,img):
    self.real=real
    self.img=img
  def showNumber(self):
    print(self.real,"i+",self.img,"j")
  def __add__(self,num2):
    newReal=self.real+num2.real
    newImg=self.img+num2.img
    return complex(newReal,newImg)
num1=complex(1,3)
num1.showNumber()
num2=complex(4,6)
num2.showNumber()
num3=num1+num2
num3.showNumber()

#-----------------------O/P:-
     1 i+ 3 j
     4 i+ 6 j

     5 i+ 9 j
