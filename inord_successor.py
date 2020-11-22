class Solution:
    def __init__(self):
        self.next_flag = False
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        def inord_next(root, p):
            if root:
                left = inord_next(root.left, p)
                if root == p:
                    self.next_flag = True
                elif self.next_flag:
                    return root
                right = inord_next(root.right, p)
                if left != None:
                    return left
                elif right != None: 
                    right
                else:
                    return None
            return None
        return inord_next(root, p)