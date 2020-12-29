import math
class Solution:
    def findPeakElement(self, nums):
        n = len(nums)
        def brute_force():
            max_peak = -math.inf
            max_peak_idx = 0
            if n == 2: 
                if nums[0] > nums[1]:
                    return 0
                else:
                    return 1
            for i in range(1, n-1):
                if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                    if nums[i] > max_peak:
                        max_peak = nums[i]
                        max_peak_idx = i
            # handling peak at end
            if nums[n-1] > max_peak:
                return n-1
            return max_peak_idx

        def bin_search(arr, l, r):
            if l < r:
                mid = (l + r) // 2
                print(mid)
                if arr[mid] > arr[l] and arr[mid] < arr[r]:
                    return bin_search(arr, mid, r)
                elif arr[mid] > arr[r] and arr[mid] < arr[l]:
                    return bin_search(arr, l, mid)
                else: 
                    l_idx = bin_search(arr, l, mid)
                    r_idx = bin_search(arr, mid, r)
                    if arr[l_idx] > arr[r_idx]:
                        return l_idx
                    else:
                        return r_idx
            return l
        bin_search(nums, 0, n-1)

if __name__ == "__main__":
    s = Solution()
    s.findPeakElement([1,2,3,4,1])
                
