#BREAK CONTROL STATEMENT
# Used to terminate the loop when encontered
i = 1
while i <= 5:
    if i == 3:            #O/P-----------1
        break                           #2
    print(i)
    i += 1

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  
#CONTINUE CONTROL STATEMENT
# Terminates the exicution in the current iteration and continue execution of the loop with the next iteration 

i = 0
while i < 5:
    i += 1                                             #O/P-----1
    if i == 3:                                                 #2
        continue                                               #4
    print(i)                                                   #5
