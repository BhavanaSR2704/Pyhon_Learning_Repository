#Creating a student class that takes name and marks of 3 subject as argument in constucttor. Then createing a method to print the average
class Student :
  def__init__(self,name,marks):
     self.name=name
     self.marks=marks
 def get_avg(self):
   sum=0
   for value in self.marks:
     sum+=val
   print("Hi",self.name,"your avg score is:",sum/3)
s1=Student("tony stark",[99,98,97])
s1.get_avg()


#-----------------O/P :- Hi tony stark your avg score is : 98.0.
