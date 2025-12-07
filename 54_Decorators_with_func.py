def square_decorator(func):
    def wrapper(num):
        print(f"Input number: {num}")
        result = func(num)
        print(f"Result: {result}")
    return wrapper

@square_decorator
def square(n):
    return n * n

square(5)


#=====================================================================

#for user input
def square_decorator(func):
    def wrapper():
        num = int(input("Enter a number: "))
        func(num)
    return wrapper

@square_decorator
def square(n):
    print("Square is:", n*n)
square()

