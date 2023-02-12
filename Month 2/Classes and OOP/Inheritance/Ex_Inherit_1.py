# Multi Level Inheritance Exercise
# Create a parent class Vehicle, and its subclasses
class Vehicle:
    def __init__(self, year, brand):
        self.year = year
        self.brand = brand
    
    def __repr__(self):
        return f"Vehicle Object"

    def __str__(self):
        return f"Year:{self.year}, Brand:{self.brand}"

v = Vehicle(2001, 'Toyota')
print(v)

class Car(Vehicle):
    def __init__(self, year, brand, model):
        super().__init__(year, brand)
        self.model = model
    
    def __str__(self):
        return super().__str__() + f", Model:{self.model}"

c = Car(2015, 'Honda', 'Civic')
print(c)

class SportsCar(Car):
    def __init__(self, year, brand, model, top_speed):
        super().__init__(year, brand, model)
        self.top_speed = top_speed
    
    def __str__(self):
        return super().__str__() + f", Top-Speed:{self.top_speed}"
        
sports = SportsCar(2013, 'Ferrari', 'LaFerrari', 350)
print(sports)

# Create a Shape Class and classes that inherit from it
class Shape:
    def calculate_area(self):
        return 0
    
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def calculate_area(self):
        return self.width * self.height

    def __str__(self):
        return f"Rectangle Object with width-{self.width} and height-{self.height}"
    
class Square(Rectangle):
    def __init__(self, side_length):
        self.side_length = side_length
    
    def calculate_area(self):
        return self.side_length * self.side_length
  
    def __str__(self):
        return f"Square Object with side-length of {self.side_length}"
    

r = Rectangle(10, 5)
print(r.calculate_area())
print(r)

s = Square(6)
print(s.calculate_area())
print(s)