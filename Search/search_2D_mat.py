class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        if m == 0: 
            return False
        n = len(matrix[0])
        row = 0
        col = n-1

        while col >= 0 and row < m:
            print(row, col) 
            if matrix[row][col] > target: 
                col -= 1
            elif matrix[row][col] < target: 
                row += 1
            else: 
                return True
        return False

if __name__ == "__main__":
    matrix = [
        [1,   4,  7, 11, 15],
        [2,   5,  8, 12, 19],
        [3,   6,  9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    s = Solution()
    print(s.searchMatrix(matrix,  9))
    print(s.searchMatrix([[1,2]],  3))