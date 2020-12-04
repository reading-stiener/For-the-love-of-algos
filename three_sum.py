from collections import Counter
class Solution1:
    # O n^3 solution.. TLE on cases > 3000 
    def threeSum(self, nums):
        nums_count = Counter()
        n = len(nums)
        three_list = set()
        for num in nums:
            nums_count[num] += 1
        doubles = []
        for i in range(n):
            for j in range(i+1, n):
                doubles.append(sorted([nums[i], nums[j]]))
        for double in doubles:
            comp = -(double[0]+double[1])
            first = double[0]
            second = double[1]
            if nums_count[comp] > 0 and nums_count[first] > 0 and nums_count[second] > 0:
                nums_count[comp] -= 1
                nums_count[first] -= 1
                nums_count[second] -= 1
                if nums_count[comp] < 0 or nums_count[first] < 0 or nums_count[second] < 0:
                    pass
                else:
                    three_list.add(tuple(sorted([first, second, comp])))
                nums_count[comp] += 1
                nums_count[first] += 1
                nums_count[second] += 1
        return list(map(lambda x : list(x), list(three_list)))

class Solution:
    # two pointer approach
    def threeSum(self, nums):
        def t_sum(nums):
            nums.sort()
            res = []
            n = len(nums)
            for i in range(n):
                res += t_sum_comp(nums, i)
            return res
        def t_sum_comp(nums, i):
            lo, hi = i+1, len(nums)-1
            comp = -nums[i]
            res = []
            while lo < hi:
                print(i,lo,hi)
                if nums[lo] + nums[hi] == comp:
                    res.append([nums[lo], nums[hi], nums[i]])
                    lo+=1
                    hi-=1
                    while lo < hi and nums[lo] == nums[lo+1]:
                        lo+=1
                elif nums[lo] + nums[hi] > comp:
                    hi -= 1
                elif nums[lo] + nums[hi] < comp:
                    lo += 1
            return res
        return t_sum(nums)

if __name__ == "__main__":
    s = Solution()
    print(s.threeSum([0,0,1,-1,2,-2]))