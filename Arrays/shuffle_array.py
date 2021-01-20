class Solution:

    def __init__(self, nums):
        self.nums = nums
        self.nums_dict = {}
        self.n = len(nums)
        for i in range(self.n):
            self.nums_dict[i] = nums[i]

        

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        """
        for i in range(self.n):
            self.nums[i] = self.nums_dict[i]
        return self.nums
        

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        """
        num_set = set(self.nums)
        #print(num_set)
        i = 0
        while len(num_set) > 0:
            self.nums[i] = num_set.pop()
            i += 1
        return self.nums
        