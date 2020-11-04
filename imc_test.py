# imc test 10/27/2020
# author: Abi Pradhan
import math
min_moves = math.inf
def minMoves(n, startRow, startCol, endRow, endCol):
    # Write your code here
    l = 1 # minimum possible number of moves
    r = n**2 # maximum possible number of moves
    global min_moves 
    while l <= r:
        mid =  (l + r) // 2
        if bfs(startRow, startCol, endRow, endCol, mid, n):
            r = min_moves - 1
        else:
            l = mid + 1
        break
    if min_moves == math.inf:
        return -1

    else: 
        return min_moves   

def bfs(startRow, startCol, endRow, endCol, move_lim, n): 
    global min_moves
    curr = (startRow, startCol, 0)
    queue = [curr]
    moves = 0
    visited = set()
    while len(queue) > 0:
        curr = queue.pop(0)
        visited.add((curr[0], curr[1]))
        print(visited)
        if curr[2] <= move_lim:
            if curr[0] == endRow and curr[1] == endCol:
                print("This ran!!!!")
                print(endRow)
                min_moves = curr[2]
                return True
            queue.extend(new_moves(curr, visited, n))
        else:
            return False
    return False
        
       
def new_moves(curr, visited, n): 
    move_list = []
    diff_r = [1, 2, 1, 2, -1, -2, -1, -2]
    diff_c = [2, 1, -2, -1, 2, 1, -2, -1]
    for i in range(8):
        if curr[0] + diff_r[i] > 0 and curr[0] + diff_r[i] < n and curr[1] + diff_c[i]  > 0 and curr[1] + diff_c[i] < n and (curr[0]+diff_r[i], curr[1]+diff_c[i]) not in visited: 
            move_list.append((curr[0] + diff_r[i], curr[1] + diff_c[i], curr[2]+1))
    print(move_list)
    return move_list


class SuperStack:
    def __init__(self):
        self.stack = []
    def push(self, val):
        self.stack.append(val)
    def pop(self):
        return self.stack.pop(-1)
    def inc(self, i, val):
        for j in range(i):
            self.stack[j] += val
    

if __name__  == "__main__":
    # tests go in here
    print(minMoves(50,4,44,4,8))