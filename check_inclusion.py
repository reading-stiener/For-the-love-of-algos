class Solution:
    def checkInclusion(self, s1, s2):
        def isperm(s1, s2, i, n): 
            s1 = "".join(sorted(list(s1)))
            s2 = "".join(sorted(list(s2[i:i+n]))) 
            print(s1, s2)
            if s1 == s2:
                return True
            else:
                return False
        n, m  = len(s1), len(s2)
        if n > m: 
            return False
        ans = False
        for i in range(0, m-n+1):
		    ans = (ans or isperm(s1, s2, i, n))
        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.checkInclusion("", "hello"))
