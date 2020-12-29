import math
class Solution:
    def maxProduct(self, nums):
        result = nums[0]
        min_so_far = nums[0]
        max_so_far = nums[0]
        n = len(nums)
        if n == 1:
            return result
        for i in range(1, n):
            min_so_far, max_so_far = min(nums[i], min_so_far*nums[i], max_so_far*nums[i]), max(nums[i], min_so_far*nums[i], max_so_far*nums[i])
            result = max(result, max_so_far)
        return result

if __name__ == "__main__": 
    s = Solution()
    print(s.maxProduct([2,-3,0,-4, 3,-9]))
    a = [1,2,3,4,5]
    print(a[::-1])