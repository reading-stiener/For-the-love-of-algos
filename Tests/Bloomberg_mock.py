# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict, deque
class Solution:
    def generate(self, numRows):
        pascal = [[] for _ in range(numRows)]
        pascal[0].append(1)
        for i in range(1, numRows):
            for j in range(0, i+1): 
                if j == 0 or j == i: 
                    pascal[i].append(1)
                else: 
                    pascal[i].append(pascal[i-1][j-1]+pascal[i-1][j])
        return pascal
        
    def widthOfBinaryTree(self, root):
        level_dict = defaultdict(lambda : None) #dict taking in min val and max node num
        def dfs_trav(root, level, node_num): 
            if root != None:
                if level_dict[level] == None: 
                    level_dict[level] = [node_num, node_num]
                else:
                    level_dict[level][0] = min(node_num, level_dict[level][0])
                    level_dict[level][1] = max(node_num, level_dict[level][1])
                dfs_trav(root.left, level+1, node_num*2)
                dfs_trav(root.right, level+1, node_num*2+1)
        dfs_trav(root, 0, 1)
        max_width = 0
        for level, node_nums in level_dict.items():
            max_width = max(max_width, node_nums[1]-node_nums[0]+1)
        return max_width

    def searchInsert(self, nums, target):
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            #print(mid)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target: 
                r = mid - 1
                #maxed = False
            else:
                l = mid + 1
                #maxed = True
        if nums[l] < target:
            return l+1
        return l 

    def findCircleNum(self, isConnected):
        unvisited = set([i for i in range(len(isConnected))])
        print(unvisited)
        counter = 0
        queue = deque()
        visited = set()
        while len(unvisited) > 0:
            counter += 1
            #print(unvisited, counter)
            queue.append(unvisited.pop())
            while len(queue) > 0:
                node = queue.popleft()
                if node in unvisited:
                    unvisited.remove(node)
                visited.add(node)
                for i in range(len(isConnected)):
                    if isConnected[node][i] == 1 and i not in visited:
                        queue.append(i)
            print(visited)
        return counter
        
        
if __name__ == "__main__": 
    s = Solution()
    test1 = [[1,1,0],[1,1,0],[0,0,1]]
    print(s.findCircleNum(test1))