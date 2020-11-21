class Solution:
    def wordBreak(self, s, wordDict):
        n = len(s)
        dp_array = [-1 for i in range(n)]
        def wb_recur(s, wordDict, start_idx):
            if start_idx >= n:
                return True
            ans = False
            if dp_array[start_idx] != -1: 
                return dp_array[start_idx]
            else: 
                for i in range(start_idx+1, n+1):
                    if s[start_idx:i] in wordDict: 
                        ans = (ans or wb_recur(s, wordDict, i))
                dp_array[start_idx] = ans
                return ans
        return wb_recur(s, wordDict, 0)

if __name__ == "__main__":
    s = Solution()
    d = ["apple", "penapple", "pen"]
    print(s.wordBreak("applepenapple", d))