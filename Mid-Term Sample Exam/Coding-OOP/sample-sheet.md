
### **Question 1: Payment Method Implementation**  
**Problem Statement:**  
Design a base class `PaymentMethod` with a method `pay(amount)`. Create derived classes `CreditCard`, `DebitCard`, and `Cash` that override the `pay()` method to print the respective payment messages.  

**Code Stub:**  
```python
class PaymentMethod:
    def pay(self, amount):
        pass

class CreditCard(PaymentMethod):
    def pay(self, amount):
        pass

class DebitCard(PaymentMethod):
    def pay(self, amount):
        pass

class Cash(PaymentMethod):
    def pay(self, amount):
        pass

# Example usage:
amount = int(input())
# Call the pay method for each payment type
```

---

### **Question 2: Shopping Cart System**  
**Problem Statement:**  
Create an `Item` class and a `ShoppingCart` class that allows adding items, removing items, and calculating the total price.  

**Code Stub:**  
```python
class Item:
    def __init__(self, name, price):
        pass

class ShoppingCart:
    def __init__(self):
        pass

    def add_item(self, name, price):
        pass

    def remove_item(self, name):
        pass

    def total_price(self):
        pass

# Example usage:
cart = ShoppingCart()
# Read input and perform operations
```

---

### **Question 3: Employee Inheritance**  
**Problem Statement:**  
Define a base class `Employee` and derive two subclasses, `Manager` and `Developer`. Override the `calculate_salary()` method with different salary structures.  

**Code Stub:**  
```python
class Employee:
    def __init__(self, name, base_salary):
        pass

    def calculate_salary(self):
        pass

class Manager(Employee):
    def __init__(self, name, base_salary, bonus):
        pass

    def calculate_salary(self):
        pass

class Developer(Employee):
    def __init__(self, name, base_salary, overtime_hours, overtime_rate):
        pass

    def calculate_salary(self):
        pass

# Example usage:
# Read input and create objects
```

---

### **Question 4: Employee Payroll with Encapsulation**  
**Problem Statement:**  
Implement an `Employee` class with private attributes for `name` and `salary`. Use getter and setter methods to manage them.  

**Code Stub:**  
```python
class Employee:
    def __init__(self, name, salary):
        pass

    def get_name(self):
        pass

    def set_name(self, name):
        pass

    def get_salary(self):
        pass

    def set_salary(self, salary):
        pass

# Example usage:
# Read input and manipulate employee details
```

---

### **Question 5: Bank Account Management**  
**Problem Statement:**  
Create a `BankAccount` class with methods to deposit, withdraw, and display the balance. Ensure that withdrawal is only allowed if sufficient balance is available.  

**Code Stub:**  
```python
class BankAccount:
    def __init__(self, account_number, balance):
        pass

    def deposit(self, amount):
        pass

    def withdraw(self, amount):
        pass

    def get_balance(self):
        pass

# Example usage:
# Create an account and perform transactions
```

---

### **Question 6: Library Management System**  
**Problem Statement:**  
Create a `Book` class and a `Library` class where users can add, remove, and search for books.  

**Code Stub:**  
```python
class Book:
    def __init__(self, title, author):
        pass

class Library:
    def __init__(self):
        pass

    def add_book(self, book):
        pass

    def remove_book(self, title):
        pass

    def search_book(self, title):
        pass

# Example usage:
# Manage book collection
```

---

### **Question 7: Online Order Processing**  
**Problem Statement:**  
Create an `Order` class that allows adding and removing products and calculating the total cost.  

**Code Stub:**  
```python
class Order:
    def __init__(self):
        pass

    def add_product(self, product, price):
        pass

    def remove_product(self, product):
        pass

    def calculate_total(self):
        pass

# Example usage:
# Create an order and perform operations
```

---

### **Question 8: Student Grade System**  
**Problem Statement:**  
Create a `Student` class that stores student details and calculates the average grade.  

**Code Stub:**  
```python
class Student:
    def __init__(self, name):
        pass

    def add_grade(self, grade):
        pass

    def calculate_average(self):
        pass

# Example usage:
# Manage student records
```

---

### **Question 9: Vehicle Inheritance**  
**Problem Statement:**  
Create a base class `Vehicle` and derive `Car` and `Bike` with a method to display information.  

**Code Stub:**  
```python
class Vehicle:
    def __init__(self, brand):
        pass

    def display_info(self):
        pass

class Car(Vehicle):
    def __init__(self, brand, doors):
        pass

    def display_info(self):
        pass

class Bike(Vehicle):
    def __init__(self, brand, type):
        pass

    def display_info(self):
        pass

# Example usage:
# Create vehicles and display their info
```

---

### **Question 10: ATM Simulation**  
**Problem Statement:**  
Create an `ATM` class with methods to withdraw, deposit, and check balance, ensuring transaction limits.  

**Code Stub:**  
```python
class ATM:
    def __init__(self, balance):
        pass

    def deposit(self, amount):
        pass

    def withdraw(self, amount):
        pass

    def check_balance(self):
        pass

# Example usage:
# Simulate ATM operations
```
