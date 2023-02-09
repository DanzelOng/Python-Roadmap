# Anonymous/Lambda Functions: functions with no name
# like first class functions, lambda functions can be assigned to a variable
func = lambda x: x % 2 == 0
print(func(3))


# returning lambda functions from regular functions
def func():
    return lambda x: x + 2

# the lambda function is returned and assigned to the variable result
result = func()
print(result(2))


# Write a lambda function that takes a list of words
# and returns a list of the length of each word
length = lambda x: [len(i) for i in x]
print(length(['ball', 'apple', 'cat']))


# Write a lambda function that takes a string and
# returns a copy of that string with the first letter capitalized
cap_string = lambda x: x.capitalize()
print(cap_string('hello'))


# Write a lambda function that takes two lists of numbers and
# returns a list of the elements that are common to both lists
intersect = lambda x, y: [i for i in x if i in y]
print(intersect([1, 5, 10, 8], [10, 2, 4, 8]))


# Write a lambda function that takes a list of numbers and
# returns the second-largest number in the list
get_2nd_largest = lambda x: [i for i in sorted(x)][-2]
print(get_2nd_largest([1, 5, 12, 11]))


# Write a lambda function to calculate the sum of
# the square of all even numbers in a given list
sum_of_squared = lambda x: sum([i ** 2 for i in x if i % 2 ==0])
print(sum_of_squared(range(5)))


# Write a lambda function to find the product of all the elements
# in a list excluding the highest and lowest value
import math
sortt = lambda x: [i for i in sorted(x)][1:-1]
result = lambda f, x: math.prod((f(x)))
print(result(sortt, [11, 1, 5, 10, 4]))


# Write a lambda function to sort a list of dictionaries
# based on the value of a specific key
dic = [
    {'name': 'holly', 'age': 21},
    {'name': 'samuel', 'age': 25},
    {'name': 'oliver', 'age': 18}
    ]
sort_dict = lambda x: [i for i in sorted(x, key=lambda x: x['age'])]
print(sort_dict(dic))


# Write a lambda expression to flatten a nested list into a single list,
# i.e., to remove all inner lists and concatenate their elements.
nested_list = [
    ['hello', 'world'],
    ['french', 'fries']
    ]
output = [''.join(list(map(lambda x: ''.join(x), nested_list)))]
print(output)