class Solution:
    def generate(self, numRows):
        pascal_t = [[] for i in range(numRows)]
        for row in range(numRows): 
            i = 0
            while i <= row: 
                if i == 0  or i == row:
                    pascal_t[row].append(1)
                else:
                    pascal_t[row].append(pascal_t[row-1][i-1]+pascal_t[row-1][i])
                i += 1

        return pascal_t
if __name__ == "__main__":
    s = Solution()
    print(s.generate(4))
