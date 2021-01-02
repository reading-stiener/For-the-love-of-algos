class Solution:
    def findBestValue(self, arr, target):
        def sum_mutated(arr, val):
            total = 0
            for num in arr:
                if num > val:
                    total += val
                else:
                    total += num 
            return abs(total - target)
        min_val = 0
        max_val = max(arr)
        mid_val = (min_val + max_val) // 2
        while min_val < max_val:
            if sum_mutated(arr, mid_val) > sum_mutated(arr, mid_val+1):
                min_val = mid_val + 1
            elif sum_mutated(arr, mid_val) <= sum_mutated(arr, mid_val+1):
                max_val = mid_val
            mid_val = (min_val + max_val) // 2
        return min_val
                

if __name__ == "__main__":
    s = Solution()
    print(s.findBestValue([4, 9, 3], 10))