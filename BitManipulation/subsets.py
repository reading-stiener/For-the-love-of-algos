class Solution:
    def subsets(self, nums):
        power_set = [[]]
        for element in nums:
            n = len(power_set)
            for i in range(n):
                copy_list = power_set[i][:]
                copy_list.append(element)
                power_set.append(copy_list)
        return power_set
    def bit_mask(self, nums):
        n = len(nums)
        nth_bit = 1 << n
        for i in range(2**n):
            bitmask = "{0:{fill}b}".format(i, fill='0')
        
if __name__ == "__main__":
    s = Solution()
    print(s.subsets([1]))
    print(s.bit_mask([1,2]))