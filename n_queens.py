class Solution:
    def solveNQueens(self, n):
        board = [["." for _ in range(n)] for _ in range(n)]
        board_configs = []
        def board_changes(r, c, unvisited, visited_new):
            for col in range(n): 
                if (r, col) in unvisited:
                    unvisited.remove((r,col))
                    visited_new.add((r,col))
            for row in range(n):
                if (row, c) in unvisited:
                    unvisited.remove((row,c))
                    visited_new.add((row,c))
            # negative diagonal
            i = 1
            while r-i >= 0 and c-i >= 0:
                if (r-i, c-i) in unvisited:
                    unvisited.remove((r-i, c-i))
                    visited_new.add((r-i, c-i))
                i += 1
            i = 1
            while r+i < n and c+i < n:
                if (r+i, c+i) in unvisited:
                    unvisited.remove((r+i, c+i))
                    visited_new.add((r+i, c+i))
                i += 1
            # positive diagonal
            i = 1
            while r+i < n and c-i >= 0:
                if (r+i, c-i) in unvisited:
                    unvisited.remove((r+i, c-i))
                    visited_new.add((r+i, c-i))
                i += 1
            i = 1
            while r-i >= 0 and c+i < n:
                if (r-i, c+i) in unvisited:
                    unvisited.remove((r-i, c+i))
                    visited_new.add((r-i, c+i))
                i += 1

        def dfs(r, c, board, idx, n, unvisited):
            visited_new = set()
            if idx == n-1:
                board[r][c] = "Q"
                board_str_list = ["".join(board[i]) for i in range(n)]
                if board_str_list not in board_configs:
                    board_configs.append(board_str_list)
                board[r][c] = "."
            else:
                unvisited.remove((r,c))
                visited_new.add((r,c))
                board_changes(r, c, unvisited, visited_new)
                board[r][c] = "Q"
                for pos in unvisited: 
                    dfs(pos[0], pos[1], board, idx+1, n, unvisited)
                # backtracking board changes
                for pos in visited_new:
                    unvisited.add((pos[0], pos[1]))
                board[r][c] = "."
        for r in range(n): 
            for c in range(n): 
                dfs(r, c, board, 0, n, set([(r, c) for c in range(n) for r in range(n)]))
        return board_configs

if __name__ == "__main__":
    s = Solution()
    print(s.solveNQueens(4)) 
    print(s.solveNQueens(8))    




            


        