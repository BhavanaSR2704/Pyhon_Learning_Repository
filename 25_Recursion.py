# When a function calls itself repeatedly is know as recursion
#SYNTAX
  #def function_name():
    # if base_condition:
    #     return value         base case (stopping condition)
    # else:
    #     return function_name()    recursive call
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def show(n):       
  if(n==0):        #base case
    return
  print(n)
  show(n-1)
show(5)

#--------------------------------------

#In factorial
def fact(n):
  if(n==0 or n==1):
    return 1
  else:
    return n*fact(n-1)
print(fact(4))
