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
if __name__ == "__main__": 
    s = Solution()
    print(s.numRollsToTarget(30, 6, 7))