import math

class Solution:
    def slowestKey(self, releaseTimes, keysPressed):
        n = len(keysPressed)
        slowest_key = keysPressed[0]
        longest = releaseTimes[0]
        for i in range(1, n):
            if longest < releaseTimes[i] - releaseTimes[i-1]: 
                slowest_key = keysPressed[i]
                longest = releaseTimes[i] - releaseTimes[i-1]
            elif longest == releaseTimes[i] - releaseTimes[i-1]:
                if slowest_key < keysPressed[i]:
                    slowest_key = keysPressed[i]
        return slowest_key

    def checkArithmeticSubarrays(self, nums, l, r):
        def check_arithmetic(arr):
            n = len(arr)
            if len(arr) < 2: 
                return False
            elif len(arr) == 2:
                return True
            else:
                diff = arr[1] - arr[0]
                for i in range(2, n):
                    if arr[i] - arr[i-1] != diff:
                        return False
                return True
        m = len(l)
        ans = []
        for i in range(m):
            arr = nums[l[i]:r[i]+1]
            arr.sort()
            ans.append(check_arithmetic(arr))
        return ans
    
    ## dfs approach didn't work
    def minimumEffortPath(self, heights):
        rows = len(heights)
        cols = len(heights[0]) 
        visited = [[-1 for j in range(cols)] for i in range(rows)]
        self.min_effort = math.inf
        def dfs(r, c, heights, visited, max_diff):
            if r == rows-1 and c == cols-1:
                self.min_effort = min(max_diff, self.min_effort)
            visited[r][c] = 1
            diff_x = [-1, 0, 0, 1]
            diff_y = [0, -1, 1, 0]
            for k in range(4):
                i, j  = r + diff_x[k], c + diff_y[k]
                print(i,j)
                if i >= 0 and  i < rows and j >= 0 and j < cols and visited[i][j] == -1:
                    max_diff = max(max_diff, (abs(heights[i][j] - heights[r][c])))
                    if  max_diff < self.min_effort:
                        dfs(i, j, heights, visited, max_diff)
            visited[r][c] = -1
            return self.min_effort
        return dfs(0, 0, heights, visited, 0)
    
                
                             

if __name__ == "__main__":
    s = Solution()
    print(s.slowestKey([12,23,36,46,62],"spuda"))
    print(s.slowestKey([9,29,49,50], "cbcd"))
    print(s.checkArithmeticSubarrays([4,6,5,9,3,7],[0,0,2],[2,3,5]))
    print(s.checkArithmeticSubarrays([-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10], [0,1,6,4,8,7], [4,4,9,7,9,10]))
    heights = [[1,2,2],[3,8,2],[5,3,5]]
    print(s.minimumEffortPath(heights))
