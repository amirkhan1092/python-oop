***20 Python OOP questions***

### **1. Definition-Based Questions (5)**  
1. **What is encapsulation in OOP?**  
2. **Explain the purpose of the `self` keyword in Python classes.**  
3. **What is the difference between a class variable and an instance variable?**  
4. **Define polymorphism with an example.**  
5. **What is an abstract class, and how is it implemented in Python?**  

---

### **2. Debug/Testing-Based Questions (5)**  
**Question 1:** Identify the error in the code below:  
```python  
class Student:  
    def __init__(name, age):  
        self.name = name  
        self.age = age  
```  
*Error:* Missing `self` in the constructor parameters.  

**Question 2:** Debug the code to ensure the abstract method is implemented:  
```python  
from abc import ABC, abstractmethod  
class Shape(ABC):  
    @abstractmethod  
    def area(self):  
        pass  

class Circle(Shape):  
    def __init__(self, radius):  
        self.radius = radius  
```  
*Error:* `Circle` does not implement `area()`.  

**Question 3:** Fix the inheritance error:  
```python  
class Animal:  
    def speak(self):  
        print("Animal sound")  

class Dog(Animal):  
    def speak(self):  
        super().speak()  
        print("Bark")  
```  
*Issue:* `super().speak()` calls `Animal.speak()` unnecessarily.  

**Question 4:** Correct the class method usage:  
```python  
class Calculator:  
    @classmethod  
    def add(cls, a, b):  
        return a + b  

result = Calculator.add(2, 3)  
print(result)  
```  
*No error. Tests understanding of class methods.*  

**Question 5:** Fix the static method:  
```python  
class Logger:  
    @staticmethod  
    def log(message):  
        print(f"Log: {message}")  

Logger.log("Error occurred")  
```  
*No error. Tests static method usage.*  

---

### **3. Output-Based Questions (10)**  
**Question 1:** What is the output?  
```python  
class A:  
    def show(self):  
        print("A")  

class B(A):  
    def show(self):  
        print("B")  

obj = B()  
obj.show()  
```  
*Output:* `B`  

**Question 2:** Predict the output:  
```python  
class Parent:  
    def __init__(self):  
        print("Parent")  

class Child(Parent):  
    def __init__(self):  
        super().__init__()  
        print("Child")  

c = Child()  
```  
*Output:*  
```  
Parent  
Child  
```  

**Question 3:** What does this code print?  
```python  
class Counter:  
    count = 0  
    def __init__(self):  
        Counter.count += 1  

a = Counter()  
b = Counter()  
print(Counter.count)  
```  
*Output:* `2`  

**Question 4:** Predict the output:  
```python  
class Vector:  
    def __init__(self, x, y):  
        self.x = x  
        self.y = y  
    def __add__(self, other):  
        return Vector(self.x + other.x, self.y + other.y)  

v1 = Vector(1, 2)  
v2 = Vector(3, 4)  
v3 = v1 + v2  
print(v3.x, v3.y)  
```  
*Output:* `4 6`  

**Question 5:** What is the output?  
```python  
class Test:  
    def __init__(self):  
        self.__private = 10  

t = Test()  
print(t.__private)  
```  
*Output:* `AttributeError` (private variable access).  

**Question 6:** Predict the output:  
```python  
class Base:  
    def method(self):  
        print("Base")  

class Derived(Base):  
    def method(self):  
        super().method()  
        print("Derived")  

d = Derived()  
d.method()  
```  
*Output:*  
```  
Base  
Derived  
```  

**Question 7:** What does this code print?  
```python  
class MyClass:  
    class_var = 5  
    def __init__(self, instance_var):  
        self.instance_var = instance_var  

obj1 = MyClass(1)  
obj2 = MyClass(2)  
print(obj1.class_var, obj2.class_var)  
```  
*Output:* `5 5`  

**Question 8:** Predict the output:  
```python  
class A:  
    def test(self):  
        print("A")  

class B(A):  
    def test(self):  
        print("B")  

class C(A):  
    def test(self):  
        print("C")  

class D(B, C):  
    pass  

d = D()  
d.test()  
```  
*Output:* `B` (due to Method Resolution Order: D → B → C → A).  

**Question 9:** What is the output?  
```python  
class Person:  
    def __init__(self, name):  
        self.name = name  
    def __str__(self):  
        return f"Person: {self.name}"  

p = Person("Alice")  
print(p)  
```  
*Output:* `Person: Alice`  

**Question 10:** Predict the output:  
```python  
from abc import ABC, abstractmethod  
class Shape(ABC):  
    @abstractmethod  
    def area(self):  
        pass  

class Square(Shape):  
    def __init__(self, side):  
        self.side = side  
    def area(self):  
        return self.side ** 2  

s = Square(4)  
print(s.area())  
```  
*Output:* `16`  

---

Let me know if you need adjustments to difficulty or topics! 🚀