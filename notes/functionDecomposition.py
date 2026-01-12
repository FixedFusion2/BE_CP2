#TE 2nd Function Decomposition
#Normal Function before decorator
def choose_letter(letter):
    print("You chose:", letter)
    print("This is with a decorator.")
choose_letter("a")
#Decorator function example
def letter_decorator(func):
    def wrapper(*args, **kwargs):
        print("Decorated function called")
        return func(*args, **kwargs)
    return wrapper

@letter_decorator
def choose_letter(letter):
    print("You chose:", letter)

choose_letter("a")

def decorator(func):
    def wrapper():
        print("Before the function call")
        func()
        print("After the function call")
    return wrapper
@decorator
def greet():
    print("Hello!")

greet()
@decorator
def add():
    print(1+1)

add()

# Do my functions need info from other functions to work?
# Does my function call another function?
# Is it a helper function?
# Is it an inner function?
# Is it a closure function?
# Is it a decorator function?
