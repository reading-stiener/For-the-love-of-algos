import math

class Solution:
    def __init__(self):
        self.min_count = math.inf
    # brute force TLE 
    def coinChange1(self, coins, amount):
        coins.sort(reverse=True)
        def coin_change(coins, idx, count, amount_left):
            print(amount_left)
            if amount_left == 0:
                self.min_count = min(self.min_count, count)
            elif idx == len(coins):
                pass
            else:
                coin_change(coins, idx+1, count, amount_left)
                while amount_left - coins[idx] >= 0:
                    amount_left -= coins[idx]
                    count += 1
                    coin_change(coins, idx+1, count, amount_left)
        coin_change(coins, 0, 0, amount)
        return self.min_count

    # dp bottom up approach
    def coinChange(self, coins, amount):
        m = amount
        dp_table = [0] + [math.inf for i in range(m)]
        for coin in coins:
            for x in range(coin, amount+1):
                dp_table[x] = min(dp_table[x], dp_table[x-coin]+1)
        return dp_table[m] if dp_table[m] != math.inf else -1
if __name__ == "__main__":
    s = Solution()
    print(s.coinChange([3,7,405,436],8839))