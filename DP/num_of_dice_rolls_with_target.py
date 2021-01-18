class Solution:
    # Brute force Gives TLE
    def numRollsToTarget(self, d, f, target):
        count = 0
        def recur(die, total, arr):
            nonlocal count
            if die == d:
                if total == target:
                    count += 1
            else:
                for i in range(1, f+1):
                    recur(die+1, total+i, arr + [i])
        recur(0, 0, [])
        return count
    # dp approach.. works! 
    def numRollsToTarget(self, d, f, target):
        count = 0
        dp_table = [[-1 for _ in range(target+1)] for _ in range(d+1)]
        dp_table[0][0] = 1
        for c in range(1, target+1):
            dp_table[0][c] = 0
        def recur(die, target):
            if dp_table[die][target] != -1:
                return dp_table[die][target]
            total_ways = 0
            for i in range(1, f+1):
                if target-i >= 0:
                    total_ways += recur(die-1, target-i)
            dp_table[die][target] = total_ways
            return dp_table[die][target]
        recur(d, target)
        return dp_table[d][target] % (10**9+7)
    
if __name__ == "__main__": 
    s = Solution()
    print(s.numRollsToTarget(30, 6, 7))