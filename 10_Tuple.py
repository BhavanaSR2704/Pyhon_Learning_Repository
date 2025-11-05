#TUPLE is a built-in data type that lets us create immutable sequences of value
#Tuple is also like a list but it is immutable

my_tuple = (10, 20, 30, 40, 50)
print(my_tuple)            #---------------O/P  (10, 20, 30, 40, 50)
                                     
                                        
----------------------------------
my_tuple = (10, 20, 30, 40, 50)
print(my_tuple[2])        #--------------O/P   30


---------------------------------
my_tuple = (10, 20, 30)
my_tuple[1] = 50   # Error   We can not make changes in tuples so it is called as immutable /neither add nor delete
