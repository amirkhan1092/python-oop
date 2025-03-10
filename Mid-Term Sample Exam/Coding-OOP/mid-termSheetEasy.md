

### **Problem 1: Student Class with GPA Calculation**
**Task**: Create a `Student` class to calculate GPA from a list of courses.  
**Input**: List of tuples `(credit, grade)` for courses.  
**Output**: GPA (float, 2 decimal places).  

```python
class Student:
    def __init__(self, name):
        self.name = name
        self.courses = []
    
    def add_course(self, credit, grade):
        self.courses.append((credit, grade))
    
    # Implement this method
    def calculate_gpa(self):
        # Logic here
        pass

# Test Input
student = Student("Alice")
student.add_course(3, 'A')
student.add_course(4, 'B')
print(f"{student.calculate_gpa():.2f}")  # Expected Output: 3.14
```

---

### **Problem 2: Inheritance with Vehicle and Car**
**Task**: Create a `Vehicle` superclass and a `Car` subclass with additional attributes.  
**Input**: `model`, `year`, `num_doors`.  
**Output**: Formatted vehicle info including doors.  

```python
class Vehicle:
    def __init__(self, model, year):
        self.model = model
        self.year = year
    
    # Override this in Car
    def display_info(self):
        return f"{self.year} {self.model}"

class Car(Vehicle):
    def __init__(self, model, year, num_doors):
        # Initialize parent and add doors
        pass
    
    # Implement this method
    def display_info(self):
        # Include num_doors in output
        pass

# Test Input
car = Car("Toyota Camry", 2020, 4)
print(car.display_info())  # Expected Output: "2020 Toyota Camry, 4 doors"
```

---

### **Problem 3: Encapsulation with BankAccount**
**Task**: Implement a `BankAccount` class with private `balance` and transaction methods.  
**Input**: `initial_balance`, followed by transactions.  
**Output**: Final balance after deposits/withdrawals.  

```python
class BankAccount:
    def __init__(self, initial_balance):
        # Initialize balance privately
        pass
    
    def deposit(self, amount):
        # Add to balance
        pass
    
    def withdraw(self, amount):
        # Subtract from balance (no overdraft)
        pass
    
    # Implement this
    def get_balance(self):
        pass

# Test Input
acc = BankAccount(100)
acc.deposit(50)
acc.withdraw(30)
print(acc.get_balance())  # Expected Output: 120
```

---

### **Problem 4: Polymorphism with Shapes**
**Task**: Create `Shape`, `Circle`, and `Rectangle` classes with `area()` method.  
**Input**: `radius` or `length`/`width`.  
**Output**: Area of the shape.  

```python
class Shape:
    def area(self):
        raise NotImplementedError

class Circle(Shape):
    def __init__(self, radius):
        # Initialize radius
        pass
    
    # Implement this
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        # Initialize dimensions
        pass
    
    # Implement this
    def area(self):
        pass

# Test Input
circle = Circle(7)
print(circle.area())  # Expected Output: ~153.94 (pi*r^2)
```

---

### **Problem 5: Composition with Library and Book**
**Task**: Create a `Library` class that manages a list of `Book` objects.  
**Input**: Book titles to add and search.  
**Output**: Search result (True/False).  

```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self):
        self.books = []
    
    # Implement this
    def add_book(self, title, author):
        pass
    
    # Implement this
    def search_by_title(self, title):
        pass

# Test Input
lib = Library()
lib.add_book("1984", "George Orwell")
print(lib.search_by_title("1984"))  # Expected Output: True
```
