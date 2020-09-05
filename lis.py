# code
# author : Abi Pradhan

# think this brute force approach was right but gives wrong ans
# not sure why
def lis_brute(arr): 
    print(arr)
    if len(arr) == 2:
        if arr[1] > arr[0]:
            return 2
        else:
            return 1
    elif len(arr) < 2:
        return len(arr)
    elif arr[-1] >= arr[-2] and arr[-1] >= arr[-3]:
        return max(1 + lis_brute(arr[:-1]),  1 + lis_brute(arr[:-2]))
    elif arr[-1] >= arr[-2]:
        return max(1 + lis_brute(arr[:-1]), lis_brute(arr[:-2]))
    elif arr[-1] >= arr[-3]:
        return max(lis_brute(arr[:-1]), 1 + lis_brute(arr[:-2])) 
    else: 
        return max(lis_brute(arr[:-1]), lis_brute(arr[:-2]))


# couldn't solve this. copied this from geek for geeks
# recursive solution with memoization

global maximum

def lis_recur(arr, n, lis_table):
    global maximum
    
    # base case
    if n == 1: 
        return 1
    
    if lis_table[n-1] != -1:
        return lis_table[n-1]
    
    # maxEndingHere
    max_end_here = 1
    for i in range(1, n):
        res = lis_recur(arr, i, lis_table)
        if arr[i-1] < arr[n-1] and res + 1 > max_end_here:
            max_end_here  = res + 1
    maximum = max(maximum, max_end_here)
    lis_table[n-1] = max_end_here
    return max_end_here 

def lis(arr):
    global maximum
    n = len(arr)
    maximum = 1
    lis_table = [-1 for i in range(n)]
    lis_recur(arr, n, lis_table)
    return maximum

# tabulation method

def lis_tab(arr):
    maximum = 1
    n = len(arr)
    lis_table = [1 for i in range(n)]
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j]:
                lis_table[i] = max(lis_table[i], 1 + lis_table[j])
        maximum = max(maximum, lis_table[i])
    print(lis_table)
    return maximum

if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        n = int(input()) 
        arr = list(map(int, input().strip().split()))
        print(lis_tab(arr))
