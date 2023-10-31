class Matrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.data = [[0] * columns for i in range(rows)]

    def get(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.columns:
            return self.data[row][col]
        else:
            raise ValueError("Invalid row or column index")

    def set(self, row, col, value):
        if 0 <= row < self.rows and 0 <= col < self.columns:
            self.data[row][col] = value
        else:
            raise ValueError("Invalid row or column index")

    def transpose(self):
        transposed = Matrix(self.columns, self.rows)
        for i in range(self.rows):
            for j in range(self.columns):
                transposed.set(j, i, self.get(i, j))
        return transposed

    def matrix_multiply(self, other):
        if self.columns != other.rows:
            raise ValueError("Matrix dimensions are not compatible for multiplication")

        result = Matrix(self.rows, other.columns)
        for i in range(self.rows):
            for j in range(other.columns):
                dot_product = sum(self.get(i, k) * other.get(k, j) for k in range(self.columns))
                result.set(i, j, dot_product)
        return result

    def apply(self, func):
        for i in range(self.rows):
            for j in range(self.columns):
                self.set(i, j, func(self.get(i, j)))

    def __str__(self):
        return "\n".join(" ".join(str(self.data[i][j]) for j in range(self.columns)) for i in range(self.rows))


matrix = Matrix(2, 3)
matrix.set(0, 0, 1)
matrix.set(0, 1, 2)
matrix.set(0, 2, 3)
matrix.set(1, 0, 4)
matrix.set(1, 1, 5)
matrix.set(1, 2, 6)

print("Original Matrix:")
print(matrix)

transpose_matrix = matrix.transpose()
print("\nTransposed Matrix:")
print(transpose_matrix)

product_matrix = matrix.matrix_multiply(transpose_matrix)
print("\nMatrix Multiplication:")
print(product_matrix)

matrix.apply(lambda x: x * 2)
print("\nApplied Transformation (Doubled Values):")
print(matrix)
