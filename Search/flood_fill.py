from collections import deque
class Solution:
    def floodFill(self, image, sr, sc, newColor):
        visited = set() # tuples of co ord (r,c)
        queue = deque()
        queue.append((sr,sc))
        color = image[sr][sc]
        rows, cols = len(image), len(image[0])
        while len(queue) >  0:
            curr = queue.popleft()
            image[curr[0]][curr[1]] = newColor
            if curr not in visited:
                options = [(curr[0]-1, curr[1]), (curr[0], curr[1]-1), (curr[0]+1, curr[1]), (curr[0], curr[1]+1)]
                for r, c in options:
                    if r >= 0 and r < rows and c >= 0 and c < cols and image[r][c] == color :
                        queue.append((r,c))
                visited.add(curr)
        return image

if __name__ == "__main__":
    s = Solution()
    print(s.floodFill([[],[],[]], 1, 1, 2))