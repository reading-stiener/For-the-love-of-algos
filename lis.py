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
def lis(arr):
    max_lis = 1
    max = -1

global maximum

def lis_recur(arr, n):
    global maximum

    # base case
    if n == 1: 
        return 1
    
    # maxEndingHere
    max_end_here = 1

    for i in range(1, n):
        res = lis_recur(arr, i)
        if arr[i-1] < arr[n-1] and res + 1 > max_end_here:
            max_end_here  = res + 1
    maximum = max(maximum, max_end_here)
    return max_end_here 

def lis(arr):
    global maximum
    n = len(arr)
    maximum = 1
    lis_recur(arr, n)
    return maximum



if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        n = int(input()) 
        arr = list(map(int, input().strip().split()))
        print(lis(arr))
