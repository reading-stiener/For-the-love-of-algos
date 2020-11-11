from collections import deque
class Solution:
    def longestWPI(self, hours):
        stack = deque()
        n =  len(hours)
        longest_int = 0
        for i in range(n):
            if hours[i] > 8:
                stack.append(hours[i])
            elif hours[i] <= 8 and len(stack)>0:
                temp_list = [hours[i]]
                while len(stack) > 0:
                    temp_list.append(stack.pop())
                    temp_list.reverse()
                if longest_int < len(temp_list):
                    longest_int = len(temp_list)
        if longest_int < len(stack):
            longest_int = len(stack)
        return longest_int

if __name__ == "__main__":
    s = Solution()
    print(s.longestWPI([9,9,6,0,6,6,9, 9, 10,12]))
    print(s.longestWPI([3,4,5,1]))