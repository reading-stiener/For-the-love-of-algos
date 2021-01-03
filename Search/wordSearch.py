class Solution:
    def exist(self, board, word):
        def dfs(row, col, visited, word, idx):
            visited.add((row, col))
            #print("visited so far ", visited)
            #print("curr {} {}".format(row, col))
            #print("curr letter ", word[idx])
            if word[idx] != board[row][col]:
                visited.remove((row, col))
                return False
            else:
                #print("row col".format(row, col))
                #print(board[row][col])
                if idx == len(word)-1: 
                    return True
                ways = adjacent(row, col, len(board), len(board[0]))
                #print(ways)
                for r, c in ways: 
                    if (r, c) not in visited and dfs(r, c, visited, word, idx+1):
                        return True
                visited.remove((row, col))
                return False
        def adjacent(row, col, rows, cols): 
            r = [0, -1, 0, 1]
            c = [-1, 0, 1, 0]
            adj = []
            for i in range(4): 
                if row+r[i] >= 0 and row+r[i] < rows and col+c[i] >= 0 and col+c[i] < cols:
                    adj.append((row+r[i], col+c[i]))
            return adj
        rows = len(board)
        cols = len(board[0])
        for i in range(rows): 
            for j in range(cols):
                #print("start from {} {} letter {}".format(i, j, board[i][j]))
                if dfs(i, j, set(), word, 0): 
                    return True
        return False
            

