# brute force approach
def subset_sum(arr):
    n = len(arr)
    if sum(arr) % 2 > 0: 
        return False
    else: 
        return ss_recur(arr, n, sum(arr) // 2)

def ss_recur(arr, n, total_rem):
    if n == 1: # base case 
        return (total_rem - arr[0]) == 0
    elif arr[n-1] == total_rem:
        return True
    elif arr[n-1] < total_rem:
        return ss_recur(arr[:-1], n-1, total_rem - arr[-1]) or \
               ss_recur(arr[:-1], n-1, total_rem)
    else:
        return ss_recur(arr[:-1], n-1, total_rem)

# dp approach. pseudopolynomial O(n*target_sum)
def subset_sum_dp(arr, target):
    n = len(arr)
    dp_table = [[0 for j in range(target+1)] for i in range(n+1)]

    for i in range(n+1):
        for j in range(target+1):
            if j == 0: # sum = 0 possible from any subset of arr
                dp_table[i][j] = 1
            elif i == 0: # sum > 0 not possible from empty subset
                dp_table[i][j] = 0
            else:
                if arr[i-1] > j:
                    dp_table[i][j] = dp_table[i-1][j]
                else:
                    dp_table[i][j] = dp_table[i-1][j-arr[i-1]] or dp_table[i-1][j]
    return dp_table[n][target]

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        target = int(input())
        arr = list(map(int, input().strip().split()))
        print(subset_sum_dp(arr, target))