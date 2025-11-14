# PASS IS A NULL STATEMENT THAT DOES NOTHING.IT IS USED AS A PLACE HOLDER FOR FUTURE CODE



for i in range(5):                #------O/P ERROR
#---------------------------
for i in range(5):
  pass                            #-----O/P NO ERROR
#------------------------------------------


age = 18
if age >= 18:
    pass   # I might add permission code later
else:
    print("Not allowed")
#-----------------------------------------------

def add_student():
    pass  # code will be added later
def view_students():
    print("Showing all students...")
view_students()
add_student()

#------------------------------------------

students = ["Rahul", "Priya", "Vivek", "Unknown"]
for name in students:
    if name == "Unknown":
        pass     # do nothing for Unknown
    else:
        print("Present:", name)

