import math
from collections import deque
class Solution:
    def verifyPreorder(self, preorder):
        stack = deque()
        min_val = -math.inf
        n = len(preorder)
        for i in range(n): 
            if preorder[i] < min_val:
                return False
            while len(stack) > 0 and stack[-1] < preorder[i]:
                min_val = stack.pop()
            stack.append(preorder[i])
        return True
    
if __name__ == "__main__":
    s = Solution()
    print(s.verifyPreorder([5,2,3,1,6]))