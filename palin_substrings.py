class Solution:
    def countSubstrings(self, s):
        n = len(s)
        dp = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for i in range(n-1, -1, -1):
            for j in range(i+1, n): 
                if s[i] == s[j]:
                    if j - i == 1: 
                        dp[i][j] = 1
                    elif dp[i+1][j-1] == 1:
                        dp[i][j] = 1                  
        tot = 0
        for l in dp:
            tot += sum(l)
        return tot
if __name__ == "__main__":
    s = Solution()
    print(s.countSubstrings("aaaaa"))