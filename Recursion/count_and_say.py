class Solution:
    def countAndSay(self, n): 
        # base case
        if n == 1: 
            return "1"
        else:
            pre_ans = self.countAndSay(n-1)
            count_ans = ""
            i = 1
            count = 1
            while i <= len(pre_ans):
                print("pre ans ", pre_ans)
                if i == len(pre_ans) or pre_ans[i] != pre_ans[i-1]: 
                    count_ans += str(count) + pre_ans[i-1]
                    count = 1
                else:
                    count += 1
                i += 1
            return count_ans

if __name__ == "__main__": 
    s = Solution() 
    print(s.countAndSay(6))