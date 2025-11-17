#We can't use the f.delete for deleting file,we have to use a module
#We useing the OS module 
#Module (like a code library) is a file written by another programmer that generally has a functions we can use .
#SYNTAX
#import os
#os.remove(file name)
import os
file_name = "practice.txt"
if os.path.exists(file_name):
    os.remove(file_name)
    print("File deleted successfully!")
else:
    print("File does not exist!")
