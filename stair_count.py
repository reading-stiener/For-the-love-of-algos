class Solution:
    def climbStairs(self, n):
        def climb_count(n): 
            dp_table = [-1 for i in range(n+1)]
            ans = climb_count_recur(0, dp_table, n)
            return ans
        def climb_count_recur(stair_count, dp_table, n): 
            if dp_table[stair_count] != -1: 
                return dp_table[stair_count]
            else: 
                if stair_count == n: 
                    dp_table[stair_count] = 1
                elif stair_count == n-1: 
                    dp_table[stair_count] = 1
                elif stair_count == n-2: 
                    dp_table[stair_count] = 2
                else: 
                    dp_table[stair_count] = climb_count_recur(stair_count+1, dp_table, n) + climb_count_recur(stair_count+2, dp_table, n)
                return dp_table[stair_count]
        return climb_count(n)

if __name__ == "__main__": 
    climb = Solution()
    print(climb.climbStairs(3))
    print(climb.climbStairs(10))

    