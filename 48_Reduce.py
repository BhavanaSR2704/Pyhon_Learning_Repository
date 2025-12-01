from functools import reduce

numbers = [1, 2, 3, 4, 5]

result = reduce(lambda a, b: a + b, numbers)

print(result)

#IT REDUCES THE LIST AND GIVE A SINGLE VALUE

#=======================O/P:-15
