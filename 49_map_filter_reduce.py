from functools import reduce

numbers = list(map(int, input("Enter numbers: ").split()))   # INPUT FROM USER,PLEASE USE SPACE WHILE ENTERING NUMBER

squared = list(map(lambda x: x*x, numbers))   # USING MAP

even_squares = list(filter(lambda x: x % 2 == 0, squared))  #USING FILTER

result = reduce(lambda a, b: a + b, even_squares)   #USING REDUCE

print("Original numbers:", numbers)
print("Squared numbers:", squared)
print("Even squares:", even_squares)
print("Sum of even squares:", result)

#=============================O/P:-
Enter numbers: 2 3 4 5 6 7 8 9 
Original numbers: [2, 3, 4, 5, 6, 7, 8, 9]
Squared numbers: [4, 9, 16, 25, 36, 49, 64, 81]
Even squares: [4, 16, 36, 64]
Sum of even squares: 120
