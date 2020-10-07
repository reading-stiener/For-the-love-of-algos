class Solution:
    # memoization approacn On^2
    def canJump(self, nums):
        n = len(nums)
        if n == 0:
            return False
        can_jump_arr = [-1 for i in range(n)]
        def can_jump1(nums, idx, n, can_jump_arr):
            if can_jump_arr[idx] != -1:
                return can_jump_arr[idx]
            else: 
                if idx + nums[idx] >= n-1:
                    return True
                else: 
                    can_jump_arr[idx] = False
                    for i in range(1, nums[idx]+1):
                        can_jump_arr[idx+i] = can_jump(nums, idx+i, n, can_jump_arr)
                        can_jump_arr[idx] = can_jump_arr[idx] or can_jump_arr[idx+i]
                    return can_jump_arr[idx]
        def can_jump(nums, n):
            i = n - 1
            start = i
            while i >= 0:
                if i + nums[i] >= start:
                    start = i
                i -= 1
            print(start)
            if start <= 0: 
                return True
            else:
                return False 
            
        #return can_jump(nums, 0, n, can_jump_arr)
        return can_jump(nums, n)
if __name__ == "__main__":
    s = Solution()
    print(s.canJump([2,3,1,1,4]))
