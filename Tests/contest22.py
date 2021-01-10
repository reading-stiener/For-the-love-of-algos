from collections import Counter
class Solution: 
    def maximumUnits(self, boxTypes, truckSize):
        boxTypes.sort(key=lambda x : x[1], reverse=True)
        print(boxTypes)
        units = 0
        boxes = 0
        for box in boxTypes:
            #print(units, boxes)
            if boxes + box[0] <= truckSize:
                units += box[1] * box[0]
                boxes += box[0]
            else:
                units += (truckSize - boxes) * box[1]
                break
        return units
    # def countPairs(self, deliciousness):
    #     count = 0
    #     def backtrack(deliciousness, pair, idx):
    #         #print(pair, idx)
    #         n = len(deliciousness)
    #         nonlocal count
    #         if len(pair) == 2:
    #             if (sum(pair) & sum(pair)-1) == 0:
    #                 print(sum(pair))
    #                 count += 1
    #         elif idx <= n:
    #             for i in range(idx, n):
    #                 backtrack(deliciousness, pair+[deliciousness[i]], i+1)
    #     backtrack(deliciousness, [], 0)
    #     return count
    def countPairs(self, deliciousness): 
        pairs = Counter()
        count = 0
        MOD = 10**9 + 7
        for item in deliciousness:
            for i in range(22):
                count += pairs[2**i-item]
                print(pairs[2**i-item], count)
            pairs[item] += 1
        return count % MOD

class Solution:
    def waysToSplit(self, nums):
        def bin_search(nums, A, l_idx, search_left):
            left_sum = A[l_idx]
            l, r = l_idx+1, n-2
            res = -1
            while l <= r:
                mid = (l+r)//2
                mid_sum = A[mid] - left_sum
                right_sum = A[n-1] - A[mid]
                if left_sum <= mid_sum and right_sum >= mid_sum:
                    res = mid
                    if search_left:
                        r = mid - 1
                    else:
                        l = mid + 1
                elif left_sum > mid_sum:
                    l = mid + 1
                else:
                    r = mid - 1
            return res
        MOD = 10**9 + 7
        n  = len(nums)
        # prefix array 
        A = [0 for _ in  range(n)]
        A[0] = nums[0]
        for i in range(1, n):
            A[i] = nums[i] + A[i-1]
        count = 0
        # going through each indexes
        for i in range(n-2): 
            left_idx = bin_search(nums, A, i, True)
            right_idx = bin_search(nums, A, i, False)
            if left_idx != -1 and right_idx != -1:
                count += right_idx - left_idx + 1
        return count % MOD
        
if __name__ == "__main__":
    s = Solution()
    #print(s.maximumUnits([[5,10],[2,5],[4,7],[3,9]],10))
    #print(s.countPairs([2160,1936,3,29,27,5,2503,1593,2,0,16,0,3860,28908,6,2,15,49,6246,1946,23,105,7996,196,0,2,55,457,5,3,924,7268,16,48,4,0,12,116,2628,1468]))
    #print(s.waysToSplit([1,2,2,2,5,0]))
    print(s.waysToSplit([1,1,1]))
    print(s.waysToSplit([2,3,5,10]))