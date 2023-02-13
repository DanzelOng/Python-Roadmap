# Inheritance: Allows a class to inherit attributes and methods from another class
# Single-Level Inheritance
class Person:
    def __init__(self, category):
        print(f"I am a {category}")
    
    def person_method(self):
        print("I am a method from Person Class")
    
    def display_details(self, category):
        return f"Category: {category}"

class Student(Person):
    def __init__(self, category, classroom):
        super().__init__(category)
        self.classroom = classroom
    
    def display_details(self, category):
        return super().display_details(category) + f", Classroom: {self.classroom}"

p = Person('Person')
s = Student('Student', '6A')

# Student is able to access the method from Person by inheriting from it
s.person_method()

# Method overriding: 
# Occurs when the subclass and superclass have the same methods defined
# Calling the method in the subclass will override the superclass
print(s.display_details('Student'))

class X:
    def __init__(self):
        self.x = True
        print("Calling from X")

    def foo(self):
        print(self.x)

class Y(X):
    def __init__(self):
        pass

# Even though Y inherits from X,
# instantiating Y does not show the print statement in the init method of X
y = Y()

# to directly call on the init method of X when instantiating Y,
# we use super()
class Y(X):
    def __init__(self):
        super().__init__()

# super() returns a temporary object of the superclass and allows the
# subclass to inherit all attributes and methods
y = Y()