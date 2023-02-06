# Iterators Exercise - 1
# Write a program to iterate over a list of dictionaries
# and print only the dictionaries that have a specific key.
class MyDict:

    def __init__(self, key, iterable):
        self.key = [key]
        self.index = 0
        self.iterable = iterable

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.iterable):
            dix = self.iterable[self.index]
            self.index += 1
            if self.key[0] in list(dix.keys()):
                return dix
        raise StopIteration()

dict_list = [
    {'foo': 12, 'bar': 14},
    {'moo': 52, 'car': 641},
    {'doo': 6, 'tar': 84},
    {'foo': 18, 'sar': 95}
    ]

d = MyDict('foo', dict_list)
for i in d:
    print(i)

# Write a program to iterate over a list of tuples and
# print only the second elements of the tuples
class MyTuple:

    def __init__(self, iterable):
        self.index = 0
        self.iterable = iterable

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.iterable):
            tup = self.iterable[self.index][1]
            self.index += 1
            return tup
        else:
            raise StopIteration()

tuple_list = [
    (9, 4),
    (9, 0),
    (9, 3),
    (9, 1)
]

t = MyTuple(tuple_list)
for i in t:
    print(i)

# Write a program to iterate over a list of
# dictionaries and count the occurrences of a specific key
class CountKey:

    def __init__(self, key, iterable):
        self.key = key
        self.index = 0
        self.counter = 0
        self.iterable = iterable

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.iterable):
            dix = self.iterable[self.index]
            self.index += 1
            if self.key in dix.keys():
                self.counter += 1
                return self.counter
        else:
            raise StopIteration

key = 'foo'
f = CountKey(key, dict_list)
count = 0
for i in f:
    count += 1
    if i:
        print(f"'{key}' key detected in Dictionary {count}: {dict_list[count-1]}")