class Solution:
    def canPartition(self, nums):
        n = len(nums)
        tot = sum(nums)
        part = tot // 2
        print(part)
        if tot % 2 != 0:
            return False
        dp_table = [[0 for j in range(n+1)] for i in range(part+1)]
        for r in range(1, part+1):
            for c in range(1, n+1):
                if dp_table[r-nums[c-1]][c-1] + nums[c-1] <= r: 
                    dp_table[r][c] = max(dp_table[r][c-1], dp_table[r-nums[c-1]][c-1] + nums[c-1])
                else:
                    dp_table[r][c] = dp_table[r][c-1]
        print(dp_table)
        print(dp_table[part][n], part)
        return part == dp_table[part][n]

if __name__ == "__main__":
    s = Solution()
    print(s.canPartition([1,2,3,4,5,6,7]))