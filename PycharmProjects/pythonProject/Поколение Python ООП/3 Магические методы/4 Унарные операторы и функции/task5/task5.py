class Matrix:
    def __init__(self, rows, cols, value=0):
        self.rows = rows
        self.cols = cols
        self.matrix = [[value] * cols for _ in range(rows)]

    def get_value(self, row, col):
        return self.matrix[row][col]

    def set_value(self, row, col, value):
        self.matrix[row][col] = value

    def __repr__(self):
        return f"Matrix({self.rows}, {self.cols})"

    def __str__(self):
        rows = (' '.join(map(str, row)) for row in self.matrix)
        return '\n'.join(rows)

    def __pos__(self):
        matrix = Matrix(self.rows, self.cols)
        for row in range(matrix.rows):
            for col in range(matrix.cols):
                matrix.set_value(row, col, self.get_value(row, col))
        return matrix

    def __neg__(self):
        matrix = Matrix(self.rows, self.cols)
        for row in range(matrix.rows):
            for col in range(matrix.cols):
                matrix.set_value(row, col, -self.get_value(row, col))
        return matrix

    def __round__(self, n):
        matrix = Matrix(self.rows, self.cols)
        for row in range(matrix.rows):
            for col in range(matrix.cols):
                matrix.set_value(row, col, round(self.get_value(row, col), n))
        return matrix

    def __invert__(self):
        matrix = Matrix(self.cols, self.rows)
        for row in range(self.cols):
            for col in range(self.rows):
                matrix.set_value(row, col, self.get_value(col, row))
        return matrix


matrix = Matrix(2, 3, 1)

plus_matrix = +matrix
minus_matrix = -matrix
invert_matrix = ~matrix

print(plus_matrix.cols, plus_matrix.rows)
print(minus_matrix.cols, minus_matrix.rows)
print(invert_matrix.cols, invert_matrix.rows)