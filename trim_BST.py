# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        if root: 
            if root.val >= low and root.val <= high: 
                root.right = self.trimBST(root.right, root.val, high)
                root.left = self.trimBST(root.left, low,  root.val)
                return root
            else: 
                if root.val > high: 
                    return self.trimBST(root.left, low, high)
                else: 
                    return self.trimBST(root.right, low, high)
        