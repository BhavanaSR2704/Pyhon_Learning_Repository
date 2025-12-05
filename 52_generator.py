#ALL GENERATORS ARE ITERABLES
#IT IS ALSO USED TO REDUCE THE MEMORY SPACE
import sys


l=[x*x for x in range(1,1001)]                           #MEMORY SPACE=8856
print(type(l))
print(sys.getsizeof(l))
# for i in l:
#     print(i)



gl=(x*x for x in range(1,1001))                          #MEMORY SPACE=200
print(type(gl))
print(sys.getsizeof(gl))
# for i in gl:
#     print(i)
