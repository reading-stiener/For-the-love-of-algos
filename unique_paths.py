class Solution:
    def uniquePaths(self, m, n):
        memo =  [[-1 for j in range(n)] for i in range(m)]
        print(memo)
        def unique_paths(row, col, memo):
            if row == m-1  or col == n-1:
                return 1
            if memo[row][col] != -1:
                return memo[row][col]
            else: 
                if row < m and col < n:
                    memo[row][col] = unique_paths(row+1, col, memo) + unique_paths(row, col+1, memo)
                elif row < m:
                    memo[row][col] = unique_paths(row+1, col, memo)
                elif col < n: 
                    memo[row][col] = unique_paths(row, col+1, memo)
                return memo[row][col]
        return unique_paths(0, 0, memo)


if __name__ == "__main__":
    s = Solution()
    print(s.uniquePaths(3,50))