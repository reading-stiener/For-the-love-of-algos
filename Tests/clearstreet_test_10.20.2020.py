import math

def hamming_distance(string1, string2): 
    n = len(string1)
    dist = 0
    for i in range(n): 
        if string1[i] != string2[i]: 
            dist += 1
    return dist
def borderSort(matrix):
    n = len(matrix)
    sorted_matrix = [["_" for i in range(n)] for j in range(n)]
    print(sorted_matrix)
    half_value = math.floor((n-1)/2)
    
    ## even case
    for i in range(half_value+1):
        temp_array = []
        # populating top row
        for j in range(i, n-i):
            temp_array.append(matrix[i][j])
        # populating right column
        for j in range(i+1, n-i): 
            temp_array.append(matrix[j][n-1-i])
        # populating bottom row
        for j in range(n-2-i, i, -1): 
            temp_array.append(matrix[n-i-1][j])
        # populating left column
        for j in range(n-1-i, i, -1):
            temp_array.append(matrix[j][0])
        temp_array.sort()
        count = 0
        # populating top row
        for j in range(i, n-i):
            matrix[i][j] = temp_array[count]
            count += 1
        # populating right column
        for j in range(i+1, n-i): 
            matrix[j][n-1-i] = temp_array[count]
            count += 1
        # populating bottom row
        for j in range(n-2-i, i, -1): 
            matrix[n-i-1][j] = temp_array[count]
            count += 1
        # populating left column
        for j in range(n-1-i, i, -1):
            matrix[j][0] = temp_array[count] 
            count += 1
    return matrix 

if __name__ == "__main__":
    #Lets go.. I got this
    matrix = [[9, 7, 4],
          [1, 6, 2],
          [12, 20, 3]]
    print(borderSort(matrix))