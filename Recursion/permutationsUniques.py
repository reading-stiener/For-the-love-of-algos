class Solution:
    def permutationUnique(self, nums): 
        perm_set = set()
        n = len(nums)
        def permutations(nums, idx):
            if idx == n-1:
                perm_set.add(tuple(nums))
            else:
                for i in range(idx, n):
                    nums[i], nums[idx] = nums[idx], nums[i]
                    permutations(nums, idx+1)
                    nums[i], nums[idx] = nums[idx], nums[i]
        permutations(nums, 0)
        return [list(num_str) for num_str in perm_set]

if __name__ == "__main__":
    s = Solution()
    print(s.permutationUnique([1,1,2]))