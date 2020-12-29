class Solution:
    def maxSubArray(self, nums):
        max_sum = nums[0]
        max_so_far = nums[0]
        if len(nums) == 1:
            return max_sum
        for i in range(1, len(nums)): 
            max_so_far = max(max_so_far + nums[i], nums[i])
            max_sum = max(max_so_far, max_sum)
        return max_sum

if __name__  == "__main__": 
    s = Solution() 
    print(s.maxSubArray([0]))