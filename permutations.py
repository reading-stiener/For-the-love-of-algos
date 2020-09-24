class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        distinct_list = []
        if len(nums) == 1: 
            return [nums]
        else: 
            for num in nums:
                nums_copy = nums[:]
                nums_copy.remove(num)
                sub_permute = self.permute(nums_copy)
                for lis in sub_permute:
                    distinct_list.append([num] + lis)
        return distinct_list