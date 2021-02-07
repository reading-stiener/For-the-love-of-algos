import math
class Solution:
    def coinChange(self, coins, amount):
        dp_table = [0] + [math.inf for i in range(amount)]
        for i in range(1, amount+1):
            for coin in coins:
                if i - coin >= 0:
                    dp_table[i] = min(dp_table[i-coin], dp_table[i])
        if dp_table[amount] == math.inf:
            return -1
        return dp_table[amount]