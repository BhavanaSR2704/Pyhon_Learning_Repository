marks=[1,2,3]
dm=[num*2 for num in marks]
print(dm)

#==================================O/P:-
[2, 4, 6]


#-----------------------------------------------------------

students=["B","H","Z"]
marks=["1","2","3"]
d={}
for i in range(3): #if we wants to calculate the add list then add len()
    d[students[i]]=marks[i]
print(d)

#===============================O/P:-
{'B': '1', 'H': '2', 'Z': '3'}
