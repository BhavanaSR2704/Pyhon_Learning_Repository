#~~~~~~~~~~~~~~~~~~~~using all methods in a single programe~~~~~~~~~~~~~~~~~~~~~~~~

my_dict = {"name": "Bhavana", "age": 19, "course": "ISE"}
my_dict.get("name")           #---------------- o/p Bhavana
my_dict.keys()                #---------------- o/p dict_keys(['name', 'age', 'course'])
my_dict.values()              #----------------o/p dict_values(['Bhavana', 19, 'ISE'])
my_dict.items()               #--------------- o/p dict_items([('name', 'Bhavana'), ('age', 19), ('course', 'ISE')])
my_dict.update({"age": 20, "college": "KIT"})   #--------- o/p {'name': 'Bhavana', 'age': 20, 'course': 'ISE', 'college': 'KIT'}
my_dict.pop("course")         #--------------- o/p {'name': 'Bhavana', 'age': 20, 'college': 'AIT'}
my_dict.popitem()             #-------------- o/p {'name': 'Bhavana', 'age': 20}
copy_dict = my_dict.copy()    #-------------- o/p {'name': 'Bhavana', 'age': 20}
my_dict.clear()               #-------------- o/p {}
print(my_dict)                #-------------o/p []

#~~~~~~~~~~~~~~final output is []~~~~~~~~~~~~~~~
