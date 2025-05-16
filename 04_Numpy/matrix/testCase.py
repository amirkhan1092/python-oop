# class Matrix:
#     def __init__(self, data: list[list[int]]):
#         self.data = data
#         self.rows = len(data)
#         self.cols = len(data[0]) if data else 0

#     def __add__(self, other: "Matrix") -> "Matrix":
#         # Implement matrix addition here
#         pass

#     def __mul__(self, other: "Matrix") -> "Matrix":
#         # Implement matrix multiplication here
#         pass

#     def __eq__(self, other: "Matrix") -> bool:
#         # Implement matrix equality check here
#         pass

#     @property
#     def transpose(self) -> "Matrix":
#         # Implement matrix transpose here
#         pass

# def read_matrix(r: int) -> list[list[int]]:
#     return [list(map(int, input().split())) for _ in range(r)]

# if __name__ == "__main__":
#     r1, c1 = map(int, input().split())
#     m1_data = read_matrix(r1)

#     r2, c2 = map(int, input().split())
#     m2_data = read_matrix(r2)

#     m1 = Matrix(m1_data)
#     m2 = Matrix(m2_data)

#     # Matrix addition
#     try:
#         print((m1 + m2).data)
#     except:
#         print("AdditionError")

#     # Matrix multiplication
#     try:
#         print((m1 * m2).data)
#     except:
#         print("MultiplicationError")

#     # Transpose
#     print(m1.transpose.data)




class Matrix:
    def __init__(self, data: list[list[int]]):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0]) if self.rows > 0 else 0

    def __add__(self, other: "Matrix") -> "Matrix":
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("AdditionError")
        result = [
            [self.data[i][j] + other.data[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ]
        return Matrix(result)

    def __mul__(self, other: "Matrix") -> "Matrix":
        if self.cols != other.rows:
            raise ValueError("MultiplicationError")
        result = [
            [
                sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))
                for j in range(other.cols)
            ]
            for i in range(self.rows)
        ]
        return Matrix(result)

    def __eq__(self, other: "Matrix") -> bool:
        return self.data == other.data

    @property
    def transpose(self) -> "Matrix":
        result = [
            [self.data[j][i] for j in range(self.rows)]
            for i in range(self.cols)
        ]
        return Matrix(result)

def read_matrix(rows: int) -> list[list[int]]:
    return [list(map(int, input().split())) for _ in range(rows)]

if __name__ == "__main__":
    r1, c1 = map(int, input().split())
    m1_data = read_matrix(r1)
    r2, c2 = map(int, input().split())
    m2_data = read_matrix(r2)

    m1 = Matrix(m1_data)
    m2 = Matrix(m2_data)

    # Matrix addition
    try:
        print((m1 + m2).data)
    except:
        print("AdditionError")

    # Matrix multiplication
    try:
        print((m1 * m2).data)
    except:
        print("MultiplicationError")

    # Transpose of m1
    print(m1.transpose.data)
