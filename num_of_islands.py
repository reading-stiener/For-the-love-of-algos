class Solution:
    def numIslands(self, grid):
        rows, cols = len(grid), len(grid[0])
        def dfs(r, c):
            #print(r,c)
            dc = [-1, 0, 1, 0]
            dr = [0, -1, 0, 1]
            grid[r][c] = "0"
            for i in range(4):
                new_r, new_c = r + dr[i], c + dc[i]   
                if new_r >= 0 and new_r < rows and new_c >= 0 and new_c < cols and grid[new_r][new_c] == "1":
                    dfs(new_r, new_c)
        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    count += 1
                    dfs(r, c)
        return count

    def numIslands2(m, n, positions): 
        

if __name__ == "__main__": 
    s = Solution()
    grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","1","0"]
    ]
    print(s.numIslands(grid))

        