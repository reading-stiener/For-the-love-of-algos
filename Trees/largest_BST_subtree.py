import math
# Definition for a binary tree node.
class Solution:
    def largestBSTSubtree(self, root):
        def inorder_traversal(root):
            # returns arr where arr[0] -> max BST, arr[1] -> min val, arr[2] -> max val
            if root != None: 
                left = inorder_traversal(root.left)
                right = inorder_traversal(root.right)
                if left[2] < root.val and right[1] > root.val: 
                    return [left[0]+right[0]+1, min(left[1], root.val), max(right[2], root.val)]
                else: 
                    return [max(left[0], right[0]), -math.inf, math.inf]  
            else:
                return [0, math.inf, -math.inf]
        ans = inorder_traversal(root)
        return ans[0]
        

