from collections import defaultdict
class Solution:
    def myAtoi(self, s):
        def clean_string(s, d):
            s_cleaned = ""
            start = False
            for char in s:
                if d[char] != None:
                    if not start and len(s_cleaned) == 0:
                        s_cleaned += char
                        start = True
                    elif start:
                        s_cleaned += char
                    else:
                        break
                elif char == " " or char == None:
                    start = False
                else:
                    break   
            return s_cleaned
        def string_to_num(s,d):
            if s == "":
                return 0
            n = len(s)
            sign = 1
            if s[0] == "-":
                sign = -1
                s = s[1:]
                n -= 1
            elif s[0] == "+":
                s = s[1:]
                n -= 1
            ans = 0
            try:
                for i in range(n): 
                    ans += 10**(n-i-1)*d[s[i]]
                return ans * sign
            except:
                return 0
        max_val = 2**31-1
        min_val = -2**31
        d = defaultdict(lambda : None, {
            "-":"-",
            "+":"+",
            "0":0,
            "1":1,
            "2":2,
            "3":3,
            "4":4,
            "5":5,
            "6":6,
            "7":7,
            "8":8,
            "9":9
        })
        s_cleaned = clean_string(s, d)
        ans = string_to_num(s_cleaned, d)
        if ans < min_val:
            return min_val
        elif ans > max_val:
            return max_val
        else:
            return ans 

        
if __name__ == "__main__":
    s = Solution()
    # print(s.myAtoi("   -4193 with words"))
    # print(s.myAtoi("gfghkfh   -4193 with words"))
    print(s.myAtoi("2424sfgaf"))