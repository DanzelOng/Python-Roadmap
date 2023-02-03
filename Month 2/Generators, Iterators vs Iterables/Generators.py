# Generators = Iterators that yield one value at a time
# the yield statement is used to create a generator function
num_list = [1,2,3,4,5]

# Creating generator functions
def square_generator(num_list):
    for value in num_list:
        yield value ** 2

# Create a generator object
g = square_generator(num_list)

# Looping through a generator
for number in g:
    print(number)

# Like Iterators, use the next() to get each value
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

# Create a Generator comprehension by wrapping the expression in parentheses
gen = (num ** 2 for num in num_list)

# list() converts the generator back to a list
list_gen = list(gen)

# Benefits of generators
# 1.  Memory efficient

# 2. Makes code more readable and simpler
# Example 1 looks more readable compared to Example 2

# Example 1
def square_generator(num_list):
    for value in num_list:
        yield value ** 2

# Example 2
def square_list(num_list):
    squared_list = []
    for value in num_list:
        squared_list.append(value**2)
    return squared_list