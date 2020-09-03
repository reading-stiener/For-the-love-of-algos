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
  
    ans = lcs_recur(A, B, lcs_table)
    return ans

def lcs_recur(A, B, lcs_table):
    a_len, b_len = len(A), len(B)
    print(a_len, b_len)
    if lcs_table[a_len][b_len]: 
        return lcs_table[a_len][b_len]
    if A[-1] == B[-1]:
        lcs_table[a_len][b_len] = 1 + lcs_recur(A[:-2], B[:-2], lcs_table)
    else: 
        lcs_table[a_len][b_len] = max(lcs_recur(A[:-2], B[:-1], lcs_table), lcs_recur(A[:-1], B[:-2], lcs_table))
    print(lcs_table)
    return lcs_table[a_len][b_len]
    
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n_a, n_b = tuple(int(x) for x in input().split())
        A = list(input().strip())
        B = list(input().strip())
        print(A, B) 
        print(lcs(A, B))