class Solution:
    def spiralOrder(self, matrix):
      def out_of_bounds(i, j, m, n): 
        if i < 0 or i >= m  or j < 0  or j >= n:
          return True
        return False
      m = len(matrix)
      n = len(matrix[0])
      visited = set()
      spiral = []
      move = "right"
      i, j = 0, 0
      
      while len(visited) < m * n:
        spiral.append(matrix[i][j])
        visited.add((i, j))
        print(i, j)
        if move == "right": 
          if out_of_bounds(i, j+1,  m, n) or (i, j+1) in visited: 
            move = "down"
            i += 1
          else:
            j += 1
        elif move == "down": 
          if out_of_bounds(i+1, j,  m, n) or (i+1, j) in visited: 
            move = "left"
            j -= 1
          else:
            i += 1
        elif move == "left": 
          if out_of_bounds(i, j-1,  m, n) or (i, j-1) in visited: 
            move = "up"
            i -= 1
          else:
            j -= 1
        elif move == "up":
          if out_of_bounds(i-1, j,  m, n) or (i-1, j) in visited: 
            move = "right"
            j += 1
          else:
            i -= 1
      print(visited)
      return spiral 

if __name__ == "__main__": 
  s = Solution()
  mat = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
  print(s.spiralOrder(mat))
  mat = [[1,2,3],[4,5,6],[7,8,9]]
  print(s.spiralOrder(mat))