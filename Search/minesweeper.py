from collections import deque
class Solution:
    def updateBoard(self, board, click):
        n, m = len(board), len(board[0])
        r, c =  click[0], click[1]
        def check_adjacent(r, c):
            dx = [0, -1, -1, -1, 0, 1, 1, 1]
            dy = [-1, -1, 0, 1, 1, 1, 0, -1]
            adjs = []
            count = 0
            for i in range(8):
                if r+dx[i] >= 0 and r+dx[i] < n and c+dy[i] >= 0 and c+dy[i] < m:
                    adjs.append((r+dx[i], c+dy[i]))
                    if board[r+dx[i]][c+dy[i]] == "M":
                        count += 1
            return (adjs, count) 
        def update_bfs(board, r, c):
            queue = deque()
            curr = (r, c)
            visited = set() 
            queue.append(curr)
            while len(queue) > 0:
                #print(visited)
                r, c = queue.popleft()
                visited.add((r, c))
                adjs, count = check_adjacent(r, c)
                if count > 0:
                    board[r][c] = str(count)
                else:
                    board[r][c] = "B"
                    for adj_r, adj_c in adjs:
                        if (adj_r, adj_c) not in visited:
                            queue.append((adj_r, adj_c))
        if board[r][c] == "M":
            board[r][c] = "X"
            return board
        elif board[r][c] == "E":
            update_bfs(board, r, c)
            return board

if __name__ == "__main__":
    s = Solution()
    test = [['E', 'E', 'E', 'E', 'E'],
            ['E', 'E', 'M', 'E', 'E'],
            ['E', 'E', 'E', 'E', 'E'],
            ['E', 'E', 'E', 'E', 'E']]
    print(s.updateBoard(test, [3,0]))