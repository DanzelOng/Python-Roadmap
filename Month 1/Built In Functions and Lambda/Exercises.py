# Write a function that takes a list of functions as an argument
# and calls each function in the list, one after the other
def add2(num):
    return num + 2

def sub2(num):
    return num - 2

lst = [add2, sub2]
def get_func(functions, value):
    for func in functions:
        if func.__name__ == 'add2':
            print(f"function {func.__name__} is called, adding 2 to {value}. Result: {func(value)}")
        else:
            print(f"function {func.__name__} is called, deducting 2 from {value}. Result: {func(value)}")
get_func(lst, 2)


# Write a function that takes a string and a function as arguments, and returns a new string
# that is the result of applying the function to each character in the string.
def sub(word):
    new = word.upper()
    return new

def convert_str(func, string):
    return func(string)

print(convert_str(sub, 'test'))


# Write a function that takes a function and a list of numbers as arguments
# and returns the first number in the list that
# satisfies the condition specified by the function.
def check_even(arr):
    for i in arr:
        if i % 2 == 0:
            return i

def get_first_even(func, arr):
    print(f"The first even number in {arr} is {func(arr)}!")

get_first_even(check_even, list(range(1,6)))


# function currying
def multiply_5(val):
    return val * 5

def divide_2(val):
    return val // 2

def outer(func1):
    def middle(func2):
        def inner(value):
            return func1(value), func2(value)
        return inner
    return middle

first_res = outer(multiply_5)
second_res = first_res(divide_2)
third_res = second_res(6)
print(third_res)
# equivalent to
print(outer(multiply_5)(divide_2)(6))