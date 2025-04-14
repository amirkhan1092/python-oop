### **Comprehensive NumPy Notes**  
**Core Concepts, Arrays, Matrix Operations, and Data Types**  

---

#### **1. Introduction to NumPy**  
- **Purpose**:  
  - Efficient numerical computing in Python.  
  - Optimized for **array/matrix operations** (faster than Python lists).  
  - Foundation for libraries like Pandas, SciPy, and Matplotlib.  

---

#### **2. Installation & Import**  
```bash
pip install numpy   # Install via terminal
```
```python
import numpy as np  # Standard convention
```

---

#### **3. Creating Arrays**  
**a. From Python Lists**:  
```python
# 1D Array
arr_1d = np.array([1, 2, 3])  

# 2D Array (Matrix)
arr_2d = np.array([[1, 2], [3, 4]])  

# 3D Array
arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
```

**b. Built-in Functions**:  
```python
zeros = np.zeros((3, 2))   # 3x2 matrix of 0s  
ones = np.ones((2, 3))     # 2x3 matrix of 1s  
identity = np.eye(4)       # 4x4 identity matrix  
random = np.random.rand(2, 3)  # 2x3 random values (0 to 1)
```

**c. Sequences**:  
```python
range_arr = np.arange(0, 10, 2)  # [0, 2, 4, 6, 8]  
linspace = np.linspace(0, 10, 5) # 5 evenly spaced values: [0., 2.5, 5., 7.5, 10.]
```

---

#### **4. Array Properties**  
| Property | Description | Example |  
|----------|-------------|---------|  
| **`ndim`** | Number of dimensions | `arr_2d.ndim` → 2 |  
| **`shape`** | Dimensions as a tuple | `arr_2d.shape` → (2, 2) |  
| **`size`** | Total elements | `arr_2d.size` → 4 |  
| **`dtype`** | Data type of elements | `arr_1d.dtype` → int32 |  

---

#### **5. Data Types (`dtype`)**  
- **Specify/Convert Types**:  
  ```python
  arr = np.array([1, 2, 3], dtype=np.float32)  # Force float32 type
  arr = arr.astype(np.int64)                   # Convert to int64
  ```
- **Common Types**:  
  `int32`, `float64`, `bool`, `string_`.

---

#### **6. Reshaping Arrays**  
- **Reshape**:  
  ```python
  arr = np.arange(1, 7)        # [1, 2, 3, 4, 5, 6]
  reshaped = arr.reshape(2, 3) # 2x3 matrix: [[1,2,3], [4,5,6]]
  ```
  - Use `-1` to auto-calculate a dimension:  
    ```python
    arr.reshape(3, -1)  # Reshapes to 3x2
    ```

---

#### **7. Matrix Operations**  
**a. Arithmetic (Element-wise)**:  
```python
a = np.array([1, 2])
b = np.array([3, 4])
print(a + b)  # [4, 6]  
print(a * b)  # [3, 8]
```

**b. Dot Product**:  
```python
dot = np.dot(a, b)  # (1*3 + 2*4) = 11
```

**c. Matrix Multiplication**:  
```python
mat1 = np.array([[1, 2], [3, 4]])  # 2x2
mat2 = np.array([[5, 6], [7, 8]])  # 2x2
result = mat1 @ mat2               # or np.matmul(mat1, mat2)
# Output: [[19, 22], [43, 50]]
```

**d. Transpose**:  
```python
mat = np.array([[1, 2], [3, 4]])
transposed = mat.T  # [[1, 3], [2, 4]]
```

**e. Aggregation**:  
```python
arr = np.array([[1, 2], [3, 4]])
print(arr.sum())       # 10  
print(arr.max(axis=0))# [3, 4] (column-wise max)  
print(arr.mean())      # 2.5
```

---

#### **8. Key Notes**  
1. **Fixed Data Type**: All elements in a NumPy array have the same `dtype`.  
2. **Memory Efficiency**: NumPy arrays are stored in contiguous memory blocks.  
3. **Reshape Rule**: Total elements must remain the same during reshaping.  
4. **Broadcasting**: NumPy auto-aligns shapes during operations (e.g., adding a scalar to an array).  

---

**Practice Exercises**:  
1. Create a 4x4 identity matrix and convert its dtype to `float32`.  
2. Reshape a 1D array of 12 elements into a 3x4 matrix and compute its row-wise sum.  
3. Multiply two 2x3 matrices (element-wise) and then compute the column-wise mean.  

---

**Cheat Sheet**:  
```python
np.array()    # Create array  
.reshape()    # Reshape array  
np.dot()      # Dot product  
.T            # Transpose  
np.sum(axis=) # Aggregation with axis  
np.zeros()    # Matrix of zeros  
np.ones()     # Matrix of ones  
```  

