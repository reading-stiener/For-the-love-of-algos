import heapq
import math
class Solution:
    # dijkstra
    def minimumEffortPath(self, heights):
        def neighbors(curr, n, m): 
            r, c = curr[0], curr[1]
            d_r = [0, -1, 0, 1]
            d_c = [-1, 0, 1, 0]
            adjs = [] 
            for i in range(4):
                if r+d_r[i] >= 0 and r+d_r[i] < n and c+d_c[i] >= 0 and c+d_c[i] < m: 
                    adjs.append((r+d_r[i], c+d_c[i]))
            return adjs
        r, c  = len(heights), len(heights[0])
        visited = set()
        weight = [(math.inf, (i,j)) for j  in range(c) for i in range(r)]
        weight[0] = (0, (0,0))
        heapq.heapify(weight)
        effort = {} 
        while len(visited) < r*c:
            #print(weight, len(visited))
            edge, curr = heapq.heappop(weight)
            if curr in visited:
                continue
            visited.add(curr)
            effort[curr] = edge
            adjacent = neighbors(curr, r, c)
            for adj in adjacent:
                #print(curr, adj)
                diff = max(abs(heights[curr[0]][curr[1]]-heights[adj[0]][adj[1]]), edge)
                heapq.heappush(weight, (diff, adj))
        #print(effort)
        return effort[(r-1,c-1)]
