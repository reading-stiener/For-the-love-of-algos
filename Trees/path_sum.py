# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        def path_sum(root, total, sum):
            if root:
                if root.left or root.right:
                    return path_sum(root.left, total+root.val, sum) or path_sum(root.right, total+root.val, sum)
                else:
                    return total+root.val == sum
                    
        return path_sum(root, 0, sum)