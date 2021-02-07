class solution:
    def numTrees(self, n):
        num = [0, 1] + [0 for i in range(2, n+1)]
        if n < 2:
            return num[n]
        for i in range(2, n+1):
            for j in range(i):
                if num[j] == 0:
                    num[i] += num[i-j-1]
                elif num[i-j-1] == 0:
                    num[i] += num[j]
                else:
                    num[i] += num[j] * num[i-j-1]
        return num[n]

if __name__ == "__main__":
    s = solution()
    print(s.numTrees(3))