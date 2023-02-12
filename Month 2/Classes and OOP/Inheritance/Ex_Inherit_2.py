class Employee:
    employee_count = 0

    def __init__(self, name, position):
        self.name = name
        self.position = position
        print("Employee Class was Called")
        Employee.employee_count += 1
    
    def __str__(self):
        return "Parent Class: Employee"

    def display_details(self):
        return f"Name: {self.name}, Position: {self.position}"

    @classmethod
    def employees_count(cls):
        return cls.employee_count

class Manager(Employee):
    def __init__(self, name, position, department):
        super().__init__(name, position)
        self.department = department
    
    def display_details(self):
        return super().display_details() + f", Department: {self.department}"

class CEO(Manager):
    def __init__(self, name, position, department, company):
        super().__init__(name, position, department)
        self.company = company
    
    def display_details(self):
        return super().display_details() + f", Company: {self.company}"

c = CEO('John', 'CEO', 'Business Development', 'Ford Motors')
print(c.display_details())

m = Manager('Hansen', 'Manager', 'Human Resource')
print(m.display_details())

e = Employee('Jackie', 'Employee')
print(e.display_details())

print(Employee.employees_count())
print(c.__dict__)
print(CEO.__mro__)