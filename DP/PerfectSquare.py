import math 
class Solution:
    # initial DP approach
    def numSquares(self, n):
        squares = []
        i = 1
        while i**2 <= n:
            squares.append(i**2)
            i += 1
        dp_table = [[math.inf for col in range(len(squares))] for row in range(n)]
        min_row = [math.inf for row in range(n)]
        for r in range(n):
            for c in range(len(squares)):
                if r+1 == squares[c]: 
                    dp_table[r][c] = 1
                elif r+1 > squares[c]:
                    dp_table[r][c] = 1+min_row[r-squares[c]]
                min_row[r] = min(min_row[r], dp_table[r][c])
        #print(dp_table)
        return min(dp_table[n-1])
    
    # same idea optimized more
    def numSquares1(self, n):
        squares = []
        i = 1
        while i**2 <= n:
            squares.append(i**2)
            i += 1
        #dp_table = [[math.inf for col in range(len(squares))] for row in range(n)]
        min_row = [math.inf for row in range(n)]
        for r in range(n):
            for c in range(len(squares)):
                if r+1 == squares[c]: 
                    min_row[r] = 1
                elif r+1 > squares[c]:
                    min_row[r] = min(min_row[r], 1+min_row[r-squares[c]])
                else:
                    break
        #print(dp_table)
        return min_row[n-1]

if __name__ == "__main__":
    s = Solution()
    print(s.numSquares(5756))