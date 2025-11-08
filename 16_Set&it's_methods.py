#Set is a collection of the unordered items
#Each elements in the set must be unique and immutable
#NOTE: SET IS MUTABLE BUT SET ELEMENTS ARE IMMUTABLE
#------------------------------------------------------------

s1={1,2,3}
s2={3,4,5}
print(s1|s2)#This is union
print(s1&s2)#This is intersection
print(s1-s2)#This is difference

#-----------------------------------------------------------
my_set = {10, 20, 30, 40, 50}

my_set.add(60)                  # o/p {10, 20, 30, 40, 50, 60}
my_set.update([70, 80])         # o/p {10, 20, 30, 40, 50, 60, 70, 80}
my_set.remove(20)               # o/p {10, 30, 40, 50, 60, 70, 80}
my_set.discard(30)              # o/p {10, 40, 50, 60, 70, 80}
my_set.pop()                    # o/p removes random element (output vary)
copy_set = my_set.copy()        # o/p same elements as my_set

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

set1.union(set2)                # o/p {1, 2, 3, 4, 5, 6}
set1.intersection(set2)         # o/p {3, 4}
set1.difference(set2)           # o/p {1, 2}      GIVE ELEMENTS ONLY IN SET1(NOT IN SET2)
set1.symmetric_difference(set2) # o/p {1, 2, 5, 6}  GIVE ELEMENTS THAT ARE IN EITHER SET1 OR SET2 BUT NOT IN BOTH

my_set.clear()                  # o/p set()
print(my_set)                 
  # -----------final output set()---------------------
