def login_required(func):
    def wrapper():
        user = input("Enter username: ")
        password = input("Enter password: ")

        if user == "Bhavana" and password == "1234":
            print("Login successful!")
            func()
        else:
            print("Login failed! Access denied.")
    return wrapper


@login_required
def dashboard():
    print("Welcome to the Dashboard")

dashboard()

