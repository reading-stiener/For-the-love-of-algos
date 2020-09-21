class Solution:
    def palin_check_odd(self, s, i): 
        n = len(s)
        count = 1
        l, r = i, i
        while(l-1 > 0 and r+1 < n and s[l] == s[r]):
            l, r = l-1, r+1 
            count += 2
        return count
    def palin_check_even(self, s, i):
        n = len(s)
        if s[i] != s[i+1]:
            return 1 
        count = 2
        l, r = i-1, i+2
        while(l-1 > 0 and r+1 < n and s[l] == s[r]):
            l, r = l-1, r+1 
            count += 1
        return count
    def longestPalindrome(self, s):
        n = len(s)
        max_len = 0
        for i in range(n-1):
            max_len = max(max_len, self.palin_check_odd(s, i), self.palin_check_even(s, i))
        return max_len

if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindrome("babad"))
    print(s.longestPalindrome("abracadabradaaaad"))