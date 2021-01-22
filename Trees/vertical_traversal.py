# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root):
        node_dict = {}
        def traverse(root, x, y):
            if root != None:
                if node_dict.get(x, None) == None:
                    node_dict[x] = {y : [root.val]}
                else: 
                    if node_dict[x].get(y, None) == None:
                        node_dict[x][y] = [root.val]
                    else:
                        node_dict[x][y].append(root.val)
                traverse(root.left, x-1, y-1)
                traverse(root.right, x+1, y-1)
        traverse(root, 0, 0)
        ans = []
        node_tup = [(key, value) for key, value in node_dict.items()]
        node_tup.sort(key=lambda x : x[0])
        for vert_x in node_tup:
            vert_tup_list = [(key, sorted(value)) for key, value in vert_x[1].items()]
            vert_tup_list.sort(key=lambda x : x[0], reverse=True)
            vert_ans = []
            for vert_nodes in vert_tup_list:
                vert_ans += vert_nodes[1]
            ans.append(vert_ans)
        return ans