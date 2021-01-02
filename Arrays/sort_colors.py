class Solution:
    # simple bubble sort approach
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1, n):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
        return nums
    
if __name__ == "__main__":
    s = Solution()
    print(s.sortColors([3,3,0,2,3,0]))