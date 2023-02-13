# Multi-Level Inheritance
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Called from Person Class")
    
    def details(self):
        return f"Name: {self.name}"

class Student(Person):
    def __init__(self, name, age, gpa, education):
        super().__init__(name, age)
        self.gpa = gpa
        self.education = education
        print("Called from Student Class")
      
class Athlete(Student):
    def __init__(self, name, age, gpa, education, sport):
        super().__init__(name, age, gpa, education)
        self.sport = sport
        print("Called from Athlete Class")
    
    def details(self):
        return f"Name: {self.name}, Sport: {self.sport}"

print(Athlete.__mro__)
a = Athlete('danzel', 20, 3.6, 'Degree', 'gym')
print(a.details())
print()

# Multiple Inheritance
class Employee:
    def __init__(self, job, salary):
        self.job = job
        self.salary = salary
        self.promoted = False
        print("Called from Employee Class")
    
    def check_promoted(self):
        return self.promoted

class Adult(Person, Employee):
    def __init__(self, name, age, job, salary, insurance):
        Person.__init__(self, name, age)
        Employee.__init__(self, job, salary)
        self.insurance = insurance
        print("Called from Adult Class")
    
    def __repr__(self):
        return "Adult Object"
      
    def __str__(self):
        return f'Adult Object: ({self.name}-{self.age}-{self.job}-{self.salary}-{self.insurance})'

print(Adult.__mro__)
adult = Adult('User', 45, 'developer', 80000, 'Aviva')
print(adult.details())
print(adult.check_promoted())