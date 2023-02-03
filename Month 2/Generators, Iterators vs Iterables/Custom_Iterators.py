# Creating a custom iterator class that behaves like range()

# What goes behind the hood
# 1. __iter__ is called and returns an iterator object
# 2. __next__ method is then called repeatedly until StopIteration is raised
# 3. the iteration ends

class MyRange:

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        while self.start < self.end:
            number = self.start
            self.start += 1
            return number
        raise StopIteration

for value in MyRange(0,5):
    print(value)

# Custom iterator that gets each individual elements in a string
class Sentence:

    def __init__(self, sentence):
        self.sentence = sentence
        self.index = 0
        self.word = self.sentence.split()

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.word):
            raise StopIteration
        else:
            word = self.word[self.index]
            self.index += 1
            return word

s = Sentence('I am a custom Iterator Class')
for word in s:
    print(word)