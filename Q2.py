class Matrix:
    def __init__(self, data):
        self.data = data

    def __add__(self, other):
        return Matrix([[self.data[i][j] + other.data[i][j] for j in range(3)] for i in range(3)])

    def __mul__(self, other):
        result = [[0] * 3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    result[i][j] += self.data[i][k] * other.data[k][j]
        return Matrix(result)

    def transpose(self):
        return Matrix([[self.data[j][i] for j in range(3)] for i in range(3)])

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])

# Example usage
m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m2 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
print("Addition:\n", m1 + m2)
print("Multiplication:\n", m1 * m2)
print("Transpose:\n", m1.transpose())