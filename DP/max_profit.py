class Solution:
    def maxProfit(self, prices, fee):
        n = len(prices)
        cash, hold = 0, -prices[0]
        for i in range(1, n):
            cash = max(cash, hold + prices[i] - fee)
            hold = max(hold, cash - prices[i])
        return cash
