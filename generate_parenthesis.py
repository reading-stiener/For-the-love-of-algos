from itertools import combinations as p 

class Solution(object):
    def generateParenthesis(self, n):
        def generate(A = []):
            if len(A) == 2*n:
                if valid(A):
                    ans.append("".join(A))
            else:
                A.append('(')
                generate(A)
                print(A)
                A.pop()
                print(A)
                A.append(')')
                generate(A)
                A.pop()
        def valid(A):
            bal = 0
            for c in A:
                if c == '(': bal += 1
                else: bal -= 1
                if bal < 0: return False
            return bal == 0

        ans = []
        generate()
        return ans


if __name__ == "__main__":
    print("Hello") 
    s = Solution()
    #s.permutations(2)
    print(s.generateParenthesis(2))    