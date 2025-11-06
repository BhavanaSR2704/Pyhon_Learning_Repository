#TUPLE SLICING
#SYNTAX
#tuple_name[start:end:step]
numbers = (10, 20, 30, 40, 50)
print(numbers[1:4])       #--------------------O/P=(20, 30, 40)

#------------------------------------------

#step value
numbers = (10, 20, 30, 40, 50) 
print(numbers[::2])        #--------------------O/P=(10, 30, 50)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#TUPLE METHODES
#Tuples have only two built-in methods
#1.count()
marks = (10, 20, 20, 30, 20, 40)
print(marks.count(20))     #--------------------O/P=3

#2.index()
marks = (10, 20, 30, 40, 50)
print(marks.index(40))     #--------------------O/P=3
