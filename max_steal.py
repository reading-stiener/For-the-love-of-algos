class Solution:
    def rob(self, nums):
        n = len(nums)
        steal_arr = [0 for i in range(n+2)]
        for i in range(2, n+2):
            steal_arr[i] = max(steal_arr[i-1], steal_arr[i-2] + nums[i-2])
        return steal_arr[n+1]

if __name__ == "__main__":
    s = Solution()
    print(s.rob([1,3,4,5,2,45,4]))