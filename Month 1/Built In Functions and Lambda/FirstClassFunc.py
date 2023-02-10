# First Class functions
# functions that are treated as an object like other objects

# 1. assignment to variable
def check_Cap(string):
    if string == string.capitalize():
        return True
    return False

result = check_Cap
print(result('Test'))


# 2. being passed as an argument or returned from a function
def add_2(x):
    return x + 2

def sub_2(y):
    return y - 2

add = add_2
sub = sub_2

# functions can also be stored in a list
ops = [add, sub]
for func in ops:
    print(f"{func.__name__} is called, result: {func(4)}")


# being used in comparison operations
y = lambda x: x % 2 == 0
z = lambda i: i % 2 != 0
print(y(4) == z(3))