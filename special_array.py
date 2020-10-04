class Solution:
    def specialArray(self, nums):
        def find_num(x, nums):
            n = len(nums)
            for i in range(n): 
                if nums[i] >= x: 
                    return n - i
            return 0
        nums.sort()
        print(nums)
        n = len(nums)
        for x in range(n+1):
            if find_num(x, nums) == x:
                return x
        return -1 
            

if __name__ == "__main__": 
    s = Solution()
    print(s.specialArray([3,5]))