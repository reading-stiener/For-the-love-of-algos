from collections import Counter
class Solution: 
    def hasGroupsSizeX(self, deck): 
        count = Counter()
        n = len(deck)
        def check(count, size):
            for card, num in count.items():
                if num % size != 0:
                    return False
            return True
        for card in deck:
            count[card] += 1
        # going through possible partitions
        for i in range(1, int(n/2)+1):
            if n % i == 0 and check(count, n//i):
                return True
        return False
    def countSquares(self, matrix):
        count = 0
        rows, cols = len(matrix), len(matrix[0])
        max_size = min(rows, cols)
        def modify_matrix():
            nonlocal matrix
            for i in range(rows):
                row_sum = 0
                for j in range(cols):
                    row_sum += matrix[i][j]
                    #print(row_sum)
                    if i != 0 and j != 0:
                        matrix[i][j] = row_sum + matrix[i-1][j]
                    elif i == 0 and j != 0:
                        matrix[i][j] = row_sum
                    elif j == 0 and i != 0:
                         matrix[i][j] += matrix[i-1][j]
        modify_matrix()
        #print(matrix)
        def count_squares(matrix, size):
            nonlocal count
            for r in range(0, rows-size+1):
                for c in range(0, cols-size+1):
                    if r == 0 and c == 0:
                        tot = matrix[r+size-1][c+size-1]
                    elif r == 0:
                        tot = matrix[r+size-1][c+size-1] - matrix[r+size-1][c-1]
                    elif c == 0:
                        tot = matrix[r+size-1][c+size-1] - matrix[r-1][c+size-1]
                    else: 
                        tot = matrix[r+size-1][c+size-1] - matrix[r-1][c+size-1] - matrix[r+size-1][c-1] + matrix[r-1][c-1]
                    if tot == size * size:
                        count += 1
        for i in range(1, max_size+1):
            count_squares(matrix, i)
        return count
