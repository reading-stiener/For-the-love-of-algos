import math
import heapq

class Solution:
    def make_ll(points): 
        
    def kClosest(self, points, K):
        def dist(pt1, pt2): 
            return math.sqrt((pt1[0]-pt2[0])**2 + (pt1[1]-pt2[1])**2)
        h = []
        or_pt = [0,0]
        for pt in points:
            heapq.heappush(h, (dist(pt, or_pt), pt))
        ans = []
        for i in range(K):
            ans.append(heapq.heappop(h)[1])
        return ans

if __name__ == "__main__": 
    s = Solution()
    print(s.kClosest([[3,3],[5,-1],[-2,4]], 2))
    