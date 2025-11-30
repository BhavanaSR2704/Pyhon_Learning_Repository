numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)


#========================O/P:-[2, 4, 6]



#using both map and filter func
numbers = list(map(int, input("Enter the list of numbers: ").split()))  #use space while entering number
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)

#====================O/P:-
Enter the list of numbers: 1 2 3 4 
Even numbers: [2, 4]
