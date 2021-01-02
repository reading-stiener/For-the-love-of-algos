class Solution:
    def palin_check_odd(self, s, i): 
        n = len(s)
        l, r = i, i
        while(l-1 >= 0 and r+1 < n):
            if s[l-1] == s[r+1]:
                l, r = l-1, r+1
            else:
                break
        print(l, r)
        return (l, r)
    
    def palin_check_even(self, s, i):
        n = len(s)
        if s[i] != s[i+1]:
            return (i, i) 
        l, r = i, i + 1
        while(l-1 >= 0 and r+1 < n):
            if s[l-1] == s[r+1]:
                l, r = l-1, r+1
            else:
                break
        return l, r
    def longestPalindrome(self, s):
        n = len(s)
        if n:
            longest_str = s[0]
        else: 
            return ''
        for i in range(n-1):
            l_e, r_e = self.palin_check_odd(s, i)
            len_even = r_e - l_e + 1
            l_o, r_o = self.palin_check_even(s, i)
            len_odd = r_o - l_o + 1
            if max(len(longest_str), len_even, len_odd) == len_even:
                longest_str = s[l_e:r_e+1]
            elif max(len(longest_str), len_even, len_odd) == len_odd:
                longest_str = s[l_o:r_o+1]
        return longest_str
        

if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindrome("babad"))
    print(s.longestPalindrome("abracadabradaaaad"))