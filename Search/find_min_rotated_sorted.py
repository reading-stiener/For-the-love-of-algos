class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n-1
        while l <= r:
            mid = (l+r) // 2
            if nums[(mid-1)%n] > nums[mid] and nums[(mid+1)%n] > nums[mid]:
                return nums[mid]
            elif nums[mid] < nums[r]:
                r = mid - 1
            else:
                l = mid + 1
        return nums[mid]