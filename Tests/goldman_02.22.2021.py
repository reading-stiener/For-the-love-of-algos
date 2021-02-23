def numOfIds(pool):
    count_eights = pool.count("8")
    count_rest = len(pool) - count_eights
    group_tens = count_rest // 10
    if count_eights <= group_tens:
        return count_eights
    else:
        eights_less = 11 - count_rest % 10
        if count_eights - group_tens >= eights_less: 
            return group_tens + 1 + (count_eights - group_tens - eights_less) // 11
        return group_tens

def maxInversions1(arr):
    count = 0
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                for k in range(j+1, n):
                    if arr[j] > arr[k]:
                        count += 1
    return count

def maxInversions(arr):
    count = 0
    n = len(arr)
    for i in range(1, n-1):
        lt_count, gt_count = 0, 0 
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                lt_count += 1
        for k in range(0, i):
            if arr[i] < arr[k]:
                gt_count += 1
        count += lt_count * gt_count
    return count
        


if __name__ == "__main__":
    print(maxInversions([5,3,4,2,1]))