import sys
import re

def doSomething(blobs, pattern):
    result = "" 
    total_count = 0
    for blob in blobs: 
        #print(re.finditer(pattern, blob))
        count = match_pattern(blob, pattern)
        result += str(count) + "|"
        total_count += count
    return result + str(total_count)

# dynamic programming approch
def match_pattern(blob, pattern):
    m, n = len(pattern), len(blob)
    dp_table = [[0 for i in range(n)] for j in range(m)]
    print(dp_table)
    # checking if start character is available
    for i in range(n): 
        if pattern[0] == blob[i]:
            dp_table[0][i] = 1
    
    # filling the rest of the dp table
    for i in range(1, n):
        for j in range(1, m): 
            if dp_table[j-1][i-1] == 1 and pattern[j] == blob[i]:
                dp_table[j][i] = 1
    return sum(dp_table[m-1])

        
for line in sys.stdin:
    splitted_input = line.split(';')
    pattern = splitted_input[0]
    blobs = splitted_input[1].split('|')
    print(pattern, blobs)
    result = doSomething(blobs, pattern)
    print(result)