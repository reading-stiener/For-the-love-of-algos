import math
class Solution:
    def minSubArrayLen(self, s, nums):
      min_length = math.inf # possible worst case
      l , r =  0, 0
      n = len(nums)
      if n == 0: 
        return 0
      total = nums[0]
      while r != n-1:
        while total < s and r+1 < n:
          r += 1
          total += nums[r]
        while l <= r and total >= s:
          min_length = min(min_length, r-l+1)
          total -= nums[l]
          l += 1
      if min_length == math.inf: 
        return 0
      return min_length

if __name__ == "__main__": 
  s = Solution()
  print(s.minSubArrayLen(100,[2,3,1,2,4,3,4,23]))        