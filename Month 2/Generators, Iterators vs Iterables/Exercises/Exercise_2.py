# Iterators Exercise - 2
# Write a program to iterate over a list of dictionaries
# and merge them based on a common key
class MergeDict:

    def __init__(self, key, iterable):
        self.key = key
        self.obj = iterable
        self.index = 0
        self.counter = {}

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.obj):
            dix = self.obj[self.index]
            self.index += 1
            if self.key in dix.keys():
                self.counter = self.counter | dix
                return dix
        else:
            raise StopIteration()


dict_list = [
    {'foo': 12, 'bar': 14},
    {'moo': 52, 'car': 41},
    {'doo': 6, 'tar': 84},
    {'foo': 18, 'sar': 95}
    ]
keyword = 'foo'
m = MergeDict(keyword, dict_list)
for i in m:
    if i:
        print(f"Detected {i} with the '{keyword}' key")
print(f"Merging them....")
print(f"Result: {m.counter}")

# Write a program to iterate over a list of strings
# and find the most common letter
class FindCommon:

    def __init__(self, str_list):
        self.s = ''.join(str_list).lower()
        self.index = 0
        self.tracker = {let: self.s.count(let) for let in self.s}

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.tracker):
            key = list(self.tracker.keys())[self.index]
            value = self.tracker[key]
            self.index += 1
            return key, value
        else:
            raise StopIteration()

    def get_most_occurrence(self):
        most_common_letter = max(self.tracker, key=self.tracker.get)
        return most_common_letter

str_list = ['danzel', 'banana']
f = FindCommon(str_list)
for letter, occur in f:
    print(f"Letter {letter}, Count: {occur}")
print(f.get_most_occurrence())

# Write a program to iterate over a list of dictionaries
# and sort them based on a common key
class SortDict:

    def __init__(self, key, iterable):
        self.key = key
        self.obj = iterable
        self.index = 0
        self.sorted_dict = sorted(self.obj, key=lambda x: self.key in x.keys(), reverse=True)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.sorted_dict):
            dix = self.sorted_dict[self.index]
            self.index += 1
            return dix
        else:
            raise StopIteration()

s = SortDict(keyword, dict_list)
print(f"Sorting dictionaries based on the {keyword} keyword...")
for dic in s:
    print(dic, end= ', ')