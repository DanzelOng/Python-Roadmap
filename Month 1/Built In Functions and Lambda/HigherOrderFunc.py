# Higher-order functions: take in other functions as an argument
# example 1: returning an inner function from an outer function
def print_hello(msg1):
    def print_world(msg2):
        return f"{msg1} {msg2}"

    return print_world

# the argument and print_world is assigned to result
result = print_hello('hello')
# result remembers the previous argument and uses it in the inner function
print(result('world'))


# example 2: getting the square of numbers in a given array
def squared(val):
    return val ** 2

def getSquare(func, arr):
    return map(func, arr)

result = list(getSquare(squared, range(1,6)))
print(result)


# example 3
# an outer function that takes no parameters, but a function as an argument in its inner function
def outer():
    def inner(func):
        print("Step 2: I am called from inner")
        return f"Result: {func(2, 3)}"

    print("Step 1: I am called from outer")
    return inner

res = outer()
print(res(pow))