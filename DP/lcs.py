# lcs : longest common subarray
# Given two strings A and B, find the longest common subarray between them
#code

def lcs(A, B):
    lcs_table = []
    for i in range(len(A)+1):
        lcs_table.append([])
        for j in range(len(B)+1):
            if i == 0 or j == 0:
                lcs_table[i].append(0)
            else: 
                lcs_table[i].append(False)
  
    ans = lcs_recur(A, B, len(A), len(B), lcs_table)
    return ans

def lcs_recur(A, B, m, n, lcs_table):
    if m == 0 or n == 0 or lcs_table[m][n]: 
        return lcs_table[m][n]
    if A[-1] == B[-1]:
        lcs_table[m][n] = 1 + lcs_recur(A[:-1], B[:-1], m-1, n-1, lcs_table)
    else: 
        lcs_table[m][n] = max(lcs_recur(A[:-1], B, m-1, n, lcs_table), lcs_recur(A, B[:-1], m, n-1, lcs_table))
    return lcs_table[m][n]
    
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n_a, n_b = tuple(int(x) for x in input().split())
        A = list(input().strip())
        B = list(input().strip())
        print(lcs(A, B))