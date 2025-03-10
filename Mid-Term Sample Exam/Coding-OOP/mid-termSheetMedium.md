

### **Problem 1: Matrix Class with Operator Overloading**
**Task**: Implement a `Matrix` class that supports `+`, `*`, and `==` operations using operator overloading.  
**Constraints**:  
- Handle matrix dimension mismatches with custom exceptions  
- Implement transpose as a property  

```python
class MatrixDimensionError(Exception):
    pass

class Matrix:
    def __init__(self, data):
        self.data = data  # 2D list
    
    # Implement these
    def __add__(self, other):
        pass
    
    def __mul__(self, other):
        pass
    
    def __eq__(self, other):
        pass
    
    @property
    def transpose(self):
        pass

# Test Input
m1 = Matrix([[1,2],[3,4]])
m2 = Matrix([[5,6],[7,8]])
print((m1 + m2).data)  # [[6,8],[10,12]]
print((m1 * m2).data)  # [[19,22],[43,50]]
print(m1.transpose.data)  # [[1,3],[2,4]]
```

---

### **Problem 2: Observer Pattern Implementation**
**Task**: Create a `Subject` class and `Observer` interface for a stock price notification system.  
**Requirements**:  
- Observers get notified when price changes  
- Prevent duplicate observers  

```python
from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, symbol, price):
        pass

class Stock(Subject):
    def __init__(self, symbol, price):
        self._observers = set()
        self.symbol = symbol
        self._price = price
    
    def attach(self, observer):
        pass
    
    def detach(self, observer):
        pass
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        pass
    
    def _notify(self):
        pass

# Test Input
class PriceAlert(Observer):
    def update(self, symbol, price):
        print(f"ALERT: {symbol} now at {price}")

apple = Stock("AAPL", 150)
alert = PriceAlert()
apple.attach(alert)
apple.price = 155  # Should trigger alert
```

---

### **Problem 3: Multiple Inheritance: Hybrid Vehicle**
**Task**: Create a `HybridCar` that inherits from both `ElectricCar` and `CombustionCar`, resolving method conflicts.  

```python
class Engine:
    def start(self):
        raise NotImplementedError

class ElectricCar(Engine):
    def start(self):
        return "Starting electric motor"
    
    def charge(self):
        return "Charging battery"

class CombustionCar(Engine):
    def start(self):
        return "Starting gasoline engine"
    
    def refuel(self):
        return "Refueling tank"

class HybridCar(?, ?):  # Fix inheritance
    def start(self):
        # Should use electric first, then combustion
        pass

# Test Input
prius = HybridCar()
print(prius.start())  # "Starting electric motor"
print(prius.refuel())  # "Refueling tank"
```

---

### **Problem 4: Abstract Class for Neural Network Layers**
**Task**: Implement an abstract `Layer` class with enforced forward/backward methods, then create `Dense` and `ReLU` subclasses.  

```python
from abc import ABC, abstractmethod
import numpy as np

class Layer(ABC):
    @abstractmethod
    def forward(self, x):
        pass
    
    @abstractmethod
    def backward(self, grad):
        pass

class Dense(Layer):
    def __init__(self, input_size, output_size):
        self.weights = np.random.randn(input_size, output_size) * 0.01
    
    # Implement these
    def forward(self, x):
        pass
    
    def backward(self, grad):
        pass

# Test Input
dense = Dense(3, 2)
print(dense.forward(np.array([[1,2,3]])))  # Should compute matrix product
```

---

### **Problem 5: Singleton Database Connection Pool**
**Task**: Implement a singleton `DatabasePool` class with connection limits.  
**Requirements**:  
- Maximum 5 connections  
- Track active connections  
- Raise custom error when pool exhausted  

```python


class DatabasePoolError(Exception):
    pass

class DatabasePool:
    _instance = None
    # logic
    
    def __new__(cls):
        # Implement singleton 
        pass
    
    def __init__(self):
        # Initialize connection pool (only once)
        pass
    
    def get_connection(self):
        pass
    
    def release_connection(self):
        pass

# Test Input
pool1 = DatabasePool()
pool2 = DatabasePool()
print(pool1 is pool2)  # Must be True
conn = pool1.get_connection()  # Should return connection
```

---

These problems test:  
1. Operator overloading and custom exceptions  
2. Observer pattern implementation  
3. Multiple inheritance and method resolution order (MRO)  
4. Abstract base classes for ML components  
5. Singleton pattern 

