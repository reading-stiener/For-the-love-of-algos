class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        if n <= 1:
            return 0
        max_val = 0
        profit_table = [[prices[j] - prices[i] if i <= j else 0 for j in range(1, n)] for i in range(n)]
        for i in range(n):
            for j in range(n-1):
                max_val = max(max_val, profit_table[i][j])
        return max_val

if __name__ == "__main__": 
    s = Solution()
    print(s.maxProfit([2,1,2,1,0,1,2]))