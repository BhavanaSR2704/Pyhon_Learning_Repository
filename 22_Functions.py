#Block of statements that perform a specific task
#We use functions because if the code redunant number of times
#SYNTAX
#def function_name(parameters):
    # block of code
    #return value
def add_numbers(a, b):
    sum = a + b
    print("Sum is:", sum)
add_numbers(5, 10)   #------------O/P Sum is: 15


#----------------------------------------------------

def multiply(a, b):
    return a * b
result = multiply(4, 5)
print("Result is:", result)   #------------O/P Result is: 20

#------------------------------------------------------
#USING  *args AND **kwargs
#*args
# It allows the function to take any number of arguments (even none).Inside the function, args becomes a tuple containing all the passed values.

def avg(*args):
    if len(args)==0:
        return 0
    return sum(args)/len(args)
print(avg(10,20,30))                #----------------------O/P 20.0


#**kwargs
#It pass any number of keyword arguments (i.e., arguments with names).

def student_info(**details):    #USING **kwargs
    for key, value in details.items():
        print(f"{key}: {value}")

student_info(name="Anand", age=22, course="Python")

#OUT PUT
#----------------
# name: Anand
# age: 22
# course: Python


