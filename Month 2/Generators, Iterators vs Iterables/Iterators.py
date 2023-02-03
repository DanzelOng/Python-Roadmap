# Iterable = objects that can be looped over and contain the dunder __iter__
num_list = [1, 2, 3, 4, 5]
# dir() gives us the methods that an object has
print(dir(num_list))

# Iterables don't have the __next__ method
# Calling next() on an iterable will result in an error
print(next(num_list))

# Iterators = contain the __next__method
# iterators can also be looped over and remembers its previous state
# iter() is used to convert an iterable to an iterator
iter_num_list = iter(num_list)

# an iterator will be exhausted once all items have been called
# the next() function is used to get the value of each iteration
print(next(iter_num_list))  # output: 1
print(next(iter_num_list))  # output: 2
print(next(iter_num_list))  # output: 3
print(next(iter_num_list))  # output: 4
print(next(iter_num_list))  # output: 5

# using next() on an exhausted iterator will raise a StopIteration Error
print(next(iter_num_list))  # StopIteration error