class Solution:
    def search(self, nums, target):
        def bin_search(nums, n, l, r, pv, target):
            if l <= r:
                mid = (l+r) // 2
                if nums[(mid+pv)%n] > target:
                    return bin_search(nums, n,  l, mid, pv, target)
                elif nums[(mid+pv)%n] < target: 
                    return bin_search(nums, n, mid+1, r, pv, target)
                else: 
                    return (mid+pv)%n

        n = len(nums)
        pivot_idx = 0
        while pivot_idx + 1 < n:
            if nums[pivot_idx] == target:
                return pivot_idx
            elif nums[pivot_idx] > nums[pivot_idx+1]:
                break
            else: 
                pivot_idx += 1
        # do binary search
        pv = pivot_idx+1
        return bin_search(nums, n, 0, n, pv, target)

if __name__ == "__main__": 
    s = Solution()
    print(s.search([4,5,6,7,0,1,2], 0))