class Matrix:
    def __init__(self, size: int):
        self.matrix = [0] * size

    def get(self, x: int, y: int) -> int | None:
        if x != y or x > len(self.matrix):
            return
        return self.matrix[x - 1]

    def set(self, x: int, y: int, value: int) -> int | None:
        if x != y or x > len(self.matrix):
            return
        self.matrix[x - 1] = value

    def print(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                if i == j:
                    print(self.matrix[i], end=" ")
                else:
                    print("0", end=" ")
            print("")


matrix = Matrix(5)
matrix.set(1, 1, 1)
matrix.set(2, 2, 2)
matrix.set(3, 3, 3)
matrix.set(4, 4, 4)
matrix.set(5, 5, 5)
matrix.print()
