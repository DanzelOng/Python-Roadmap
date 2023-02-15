# Lesson 1: Altering our functions without modifying the code or using decorators
def divide(a, b):
    return a / b

print(divide(4, 2))

# To alter the functionality of a function without any changes to code,
# we create a decorator function

# A decorator function called smart_divide is created
def smart_divide(func):
    # inner decorates the function we pass in through smart_divide
    def inner(a, b):
        print(f"I am going to divide {a} and {b}")
        if b == 0:
            return "Opps! Cannot divide by 0."
        return func(a, b)
    return inner

# the inner function is returned and assigned to 'divide',
# essentially replacing the original divide function
divide = smart_divide(divide)

# now divide will be able to detect for any zero values
print(divide(4, 0))
print()

# Lesson 2: Decorating our functions using decorators
# We decorate our functions by adding @ followed by the decorator function

def decorater(func):
    def inner():
        print(f"Executing function {func.__name__}")
        func()
        print(f"Execution completed")
    return inner

@decorater
def y():
    print("Hello World!")

# using decorators eliminates the need to assign our function to
# the decorator function
y()

# Practical examples of Decorators
# Checking how long a function is run for
def limit_func(func):
    import time
    def inner(x, y):
        print(f"Running {x} rounds of function")
        print(f"Limiting function by {y} seconds per iteration...")
        for i in range(x):
            func(x)
            time.sleep(y)
            print(f"Round {i+1} completed")
        print("Execution completed")
    return inner

@limit_func
def iterate(x):
    for _ in range(x):
        pass