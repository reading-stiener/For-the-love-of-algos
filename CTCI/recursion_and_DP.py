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

    def perm_without_dups(self, string):
        str_list = list(string)
        permutations = []
        n = len(string)
        def perm(str_list, idx, n, permut):
            if idx == n:
                permutations.append(permut)
            for i in range(idx, n):
                str_list[idx], str_list[i] = str_list[i], str_list[idx]
                perm(str_list, idx+1, n, permut+str_list[idx])
                str_list[idx], str_list[i] = str_list[i], str_list[idx]
        perm(str_list, 0, n, "")
        return permutations

    def parens(self, n): 
        paren_list = []
        def paren_recur(n, paren, count, open_count):
            if len(paren) == 2*n: 
                paren_list.append(paren)
            else:
                if count > 0:
                    if open_count < n:
                        paren_recur(n, paren+"(", count+1, open_count+1)
                    paren_recur(n, paren+")", count-1, open_count)
                else:
                    paren_recur(n, paren+"(", count+1, open_count+1)
        paren_recur(n, "", 0, 0)
        return paren_list
    
    def coins(self, n):
        count = [[0 for i in range(n+1)] for j in range(4)]
        def coins_recur(n, denoms, idx):
            if n == 0:
                return 1
            elif n < 0 or idx > 3:
                return 0
            elif count[idx][n] != 0:
                return count[idx][n]
            else:
                for i in range(n//denoms[idx]+1):
                    count[idx][n] += coins_recur(n-denoms[idx]*i, denoms, idx+1)
            return count[idx][n]
        coins_recur(n, [25, 10, 5, 1], 0)
        print(count)
        return count[0][n]
if __name__ == "__main__":
    s = Solution()
    # print(s.magic_index([0,2,3]))
    # print(s.recursive_multiply(2,3))
    # print(s.recursive_multiply(4,66))
    # print(s.towers_of_hanoi("A", "B", "C", 3))
    #print(s.perm_without_dups("abc"))
    #print(s.parens(4))
    print(s.coins(10))