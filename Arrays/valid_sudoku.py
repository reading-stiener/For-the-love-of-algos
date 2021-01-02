class Solution:
    def isValidSudoku(self, board):
        n = len(board)
        # validating rows
        for i in range(n):
            num_check = {}
            for j in range(n):
                if board[i][j] != "." and num_check.get(board[i][j], 0):
                    return False
                else: 
                    num_check[board[i][j]] = 1
          # validating columns
        for i in range(n):
            num_check = {}
            for j in range(n):
                if board[j][i] != "." and num_check.get(board[j][i], 0):
                    return False
                else: 
                    num_check[board[j][i]] = 1

        # validating 3 x 3s
        for r in [0, 3, 6]:
            for c in [0, 3, 6]:
                num_check = {} 
                for sub_row in range(r, r+3):
                    for sub_col in range(c, c+3):
                        if board[sub_row][sub_col] != "." and num_check.get(board[sub_row][sub_col], 0):
                            print(num_check)
                            return False
                        else: 
                            num_check[board[sub_row][sub_col]] = 1
                print(num_check)
        return True 

if __name__ == "__main__": 
    s = Solution()
    test1 = [
        ["8","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    print(s.isValidSudoku(test1))