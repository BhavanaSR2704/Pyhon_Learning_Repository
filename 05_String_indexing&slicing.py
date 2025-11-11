#INDEXING:- Accessing a single character from a string using its position.
#SYNTAX----->string_variable[index]
name = "PYTHON"
print(name[0])   # P --------------O/P
print(name[2])   # T --------------O/P
print(name[-1])  # N --------------O/P
print(name[-3])  # H --------------O/P



#slicing:-Extracting a specific part [substring] from a string using a range of positions.
#SYNTAX---------->string_variable[start : end : step]
text = "HelloWorld"
print(text[0:5])     # Hello --------------O/P
print(text[5:10])    # World  --------------O/P
print(text[:5])      # Hello --------------O/P
print(text[5:])      # World  --------------O/P
print(text[0:10:2])  # Hlool --------------O/P
print(text[::-1])    # dlroWolleH --------------O/P

