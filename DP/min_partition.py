from copy import deepcopy
import math

# brute force approach, recursively find all possible combinations and find the minimum difference
def min_par_recur(arr, parts):
    if len(arr) == 1:
        parts.append(arr)
        parts.append([])
        return parts
    else:
        parts = min_par_recur(arr[:-1], parts)
        parts_copy = deepcopy(parts)
        for subset in parts_copy:
            subset.append(arr[-1])
        parts.extend(parts_copy)
        return parts

def min_par(arr):
    pars = []
    return min_par_recur(arr, pars)

def find_min_part(arr):
    abs_min = math.inf
    parts = min_par(arr)
    for part in parts: 
        abs_min = min(abs_min, abs(sum(arr) -  2 * sum(part)))
    return abs_min

# dp approach.. took help from geek for geeks

def min_part_dp(arr):
    n = len(arr) # length of array
    m = sum(arr) # total weight of array

    dp_table = [[0 for j in range(n+1)] for i in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0:
                dp_table[i][j] = 1 # can make sum == 0 for any subset
            elif j == 0:
                dp_table[i][j] = 0 # cannot make sum > 0 with empty subset
            else:
                if arr[j-1] > i:
                    dp_table[i][j] = dp_table[i][j-1]
                else:
                    dp_table[i][j] = dp_table[i-arr[j-1]][j-1] or dp_table[i][j-1]

    # figuring out the abs min of partition diff
    min_diff = m # upper bound for diff
    for j in range(m//2, -1, -1):
        if dp_table[j][n] == 1: 
            min_diff = min(min_diff, abs(2*j-m))

    return min_diff 

arr = [ 3, 1, 4, 2, 2, 1,43, 32, 342, 234]
print(find_min_part(arr))
print(min_part_dp(arr))