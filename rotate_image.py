class Solution:

    # approach 1: transpose and reverse
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        # transpose the matrix
        print(1)
        n = len(matrix)
        for i in range(n): 
            for j in range(i, n): 
                if i != j: 
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # reverse arrays
        n_half = n // 2
        for i in range(n): 
            for j in range(n_half): 
                matrix[i][j], matrix[i][n-j-1] = matrix[i][n-j-1], matrix[i][j]
        print(matrix)
        
def main():
    test_arr1 = [
        [1,2,3], 
        [4,5,6],
        [7,8,9]
    ]
    print(test_arr1)
    sol = Solution()
    sol.rotate(test_arr1)

if __name__ == "main":
    main() 

    