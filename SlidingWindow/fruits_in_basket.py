class Solution:
    def totalFruit(self, tree):
        n = len(tree)
        max_basket_count = 0
        for i in range(n):
            basket_set = set()
            basket_count = 0
            for j in range(i, n):
                if len(basket_set) < 2 and tree[j] not in basket_set: 
                    basket_set.add(tree[j])
                    basket_count += 1
                elif len(basket_set) <= 2 and tree[j] in basket_set:
                    basket_count += 1
                else: 
                    break
            max_basket_count = max(max_basket_count, basket_count)
        return max_basket_count
    
    def totalFruit_better(self, tree):
        l, r, basket_dict = 0, 0, {}
        n = len(tree)
        ans = 0
        while r < n:
            if basket_dict.get(tree[r], -1) == -1:
                basket_dict[tree[r]] = 1
            else:
                basket_dict[tree[r]] += 1  
            while len(basket_dict) > 2:
                basket_dict[tree[l]] -= 1
                if not basket_dict[tree[l]]:
                    del basket_dict[tree[l]]
                l += 1
            ans = max(ans, r-l+1)
            r += 1
        return ans

if __name__ == "__main__": 
    s = Solution()
    print(s.totalFruit_better([1,2,1]))