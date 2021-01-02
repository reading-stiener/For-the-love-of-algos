class NumMatrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def sumRegion(self, row1, col1, row2, col2):
        total = 0
        for r in range(row1, row2+1):
            for c in range(col1, col2+1):
                total += self.matrix[r][c]
        return total

if __name__ == "__main__":
    matrix =  [
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5]
    ]
    s = NumMatrix(matrix)
    print(s.sumRegion(2, 1, 4, 3))