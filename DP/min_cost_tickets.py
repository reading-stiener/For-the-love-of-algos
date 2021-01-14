class Solution:
    def mincostTickets(self, days, costs):
        n, m = len(days), len(costs)
        last_day = days[n-1]
        dp_table = [0 for i in range(last_day)]
        days[0] = costs[0]
        for i in range(2, last_day):
            if i - 1 >= 30:
                dp_table[i - 1] = min(
                    costs[2] + dp_table[i-31],
                    costs[1] + dp_table[i-8],
                    costs[0] + dp_table[i-2]
                )
            elif i - 1 >= 15:
                dp_table[i - 1] = min(
                    costs[2],
                    costs[1] + dp_table[i-8],
                    costs[0] + dp_table[i-2]
                )
            else:
                dp_table[i - 1] = min(
                    costs[2],
                    costs[1],
                    costs[0] + dp_table[i-2]
                )
        return dp_table[last_day-1]

                
                