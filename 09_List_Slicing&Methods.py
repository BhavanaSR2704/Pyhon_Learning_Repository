#It is similar to string slicing and also it is mutable
#SYNTAX
#list_name[start:end:step]
marks = [10,20,30,40,50,]        #indexing always starts from 0 to n-1
print(marks[1:4])               #--------------------o/p=[20,30,40]

#--------------------------------------------------------------------------------------

#LIST METHODS

#one single example 
my_marks=[10,20,30,40,50,]         
result=my_marks[:len(my_marks)]         #Slicing from index 0 to last using len()
print(result)
#~~~~~~~~~~~~~~~~~~~~using all methods in a single programe~~~~~~~~~~~~~~~~~~~~~~~~
my_marks = [10, 20, 30, 40, 50]

my_marks.append(60) #----------------------o/p [10,20,30,40,50,60]
my_marks.insert(2, 25)#--------------------o/p [10, 20, 25, 30, 40, 50]
my_marks.remove(40)#------------------------o/p  [10, 20, 30, 50]
my_marks.pop(3)#------------------------o/p [10, 20, 30, 50]
my_marks.sort()#------------------------o/p [10, 20, 30, 40, 50] 
my_marks.reverse()#------------------------o/p [50, 40, 30, 20, 10]
my_marks.clear()#------------------------o/p []
print(my_marks)

#THE FINAL OUT PUT FOR THIS IS EMPTY LIST [] 
