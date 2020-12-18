# CTCI recursion and DP
class Solution:
    def magic_index(self, arr):
        l, r = 0, len(arr)
        while l <= r:
            mid =  (l + r) // 2
            print(mid)
            if arr[mid] == mid:
                return mid
            elif arr[mid] > mid:
                r = mid - 1
            else:
                l = mid + 1
        return -1
    def recursive_multiply(self, a, b):
        multiple = max(a, b)
        factor = min(a, b)
        def multiply(count, multiple):
            if count == 0:
                return 0
            else:
                return multiple + multiply(count-1, multiple)
        return multiply(factor, multiple)
    def towers_of_hanoi(self, a, b, c, n): 
        if n == 1:
            print("{} -> {}".format(a, c))
        else:
            self.towers_of_hanoi(a, c, b, n-1)
            print("{} -> {}".format(a, c))
            self.towers_of_hanoi(b, a, c, n-1)

if __name__ == "__main__":
    s = Solution()
    print(s.magic_index([0,2,3]))
    print(s.recursive_multiply(2,3))
    print(s.recursive_multiply(4,66))
    print(s.towers_of_hanoi("A", "B", "C", 3))