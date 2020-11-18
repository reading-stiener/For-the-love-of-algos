from collections import deque
class Solution:
    def longestWPI(self, hours):
        res, n = 0, len(hours)
        seen = {}
        score = 0
        for i in range(n):
            score=score+1 if hours[i] > 8 else score-1
            if score > 0:
                res = i + 1
            else:
                if seen.get(score, None) == None:
                    seen[score] = i
                if seen.get(score-1, None) != None:
                    print("This")
                    res = max(i-seen[score-1], res)
        return res
    

if __name__ == "__main__":
    s = Solution()
    print(s.longestWPI([6,9,6]))