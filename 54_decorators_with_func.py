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
