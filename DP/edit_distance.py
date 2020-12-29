#code
def edit_distance_tab(str1, str2):
    m, n = len(str1),len(str2)
    opt_table = [[0 for j in range(n+1)] for i in range(m+1)]
    
    # simply delete to match 
    for j in range(n+1):
        opt_table[0][j] = j
    
    # simply insert to match
    for i in range(m+1):
        opt_table[i][0] = i
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            if str1[i-1] != str2[j-1]: 
                opt_table[i][j] = min(
                    1 + opt_table[i-1][j-1],
                    1 + opt_table[i-1][j],
                    1 + opt_table[i][j-1]
                )
            else:
                 opt_table[i][j] = opt_table[i-1][j-1]
    return opt_table[m][n]
    
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        m, n = tuple(int(x) for x in input().strip().split())
        str1, str2 = tuple(x for x in input().strip().split())
        print(edit_distance_tab(str1, str2))