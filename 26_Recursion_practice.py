# Recursion function to calculate the sum of first n natural numbers
def cal_sum(n):
  if(n==0):
    return 0
  return cal_sum(n-1)+n
sum=cal_sum(5)
print(sum)       #-----------O/P 15

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Recursive function to print all elements in a list

def print_list(list,idx=0):
  if(idx==len(list)):
    return
  print(list[idx])                                             #----O/P mango
  print_list(list,idx+1)                                              #litch
fruit=["mango","litch","apple","banana"]                              #apple
print_list(fruits)                                                    #banana
