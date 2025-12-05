def greet_decorator(func):
    def wrapper():
        print("Hello!")
        func()
        print("Welcome to Python decorators")
    return wrapper

@greet_decorator
def say_name():
    print("My name is Bhavana")

say_name()

