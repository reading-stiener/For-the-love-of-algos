class Solution:

    ## doesn't work with all edge cases, would've
    # uf lines were in ascending order
    def maxArea1(self, height):
        n = len(height)
        def max_area_help(height, l, r):
            print(l,r)
            # base case
            if r - l < 2:
                return 0
            else:
                mid_idx = (l + r) // 2 
                left_area = max_area_help(height, l, mid_idx)
                right_area = max_area_help(height, mid_idx, r)
                big_area = (r - l) * min(height[l], height[r])
                return max(big_area, left_area, right_area)
        return max_area_help(height, 0, n-1)

    ## BRUTE FORCE
    def maxArea2(self, height):
        max_area = 0
        n = len(height)
        for i in range(n-1): 
            for j in range(i+1, n):
                new_area = (j-i) * min(height[j],height[i])
                max_area = max(max_area, new_area)
        return max_area

    # O(n) approach.. took help
    def maxArea(self, height): 
        l = 0 
        r = len(height)-1
        max_area = 0
        while l != r: 
            max_area = max(max_area, (r-l) * min(height[l], height[r]))
            if height[l] < height[r]:
                l += 1
            else: 
                r -= 1
        return max_area

if __name__ == "__main__": 
    s = Solution()
    heights1 = [2,3,4,5,18,17,6]
    print(s.maxArea(heights1))