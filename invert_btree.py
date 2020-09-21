# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root):
        if root:
            if root.right or root.left: 
                root.left, root.right = root.right, root.left
            invertTree(root.left)
            invertTree(root.right)
        return root