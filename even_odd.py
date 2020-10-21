class Solution:
    def isEvenOddTree(self, root):
        level_list = {}
        def even_odd(root, level): 
            if root: 
                left_ans = even_odd(root.left, level+1)
                # append to list and check
                if level_list.get(level, -1) != -1:
                    if level_list[level] % 2 == 0 and root.val % 2 == 1 and root.val >  level_list[level]: 
                        level_list[level].append(root.val)    
                        curr_ans = True
                    elif level_list[level] % 2 == 1 and root.val % 2 == 0 and root.val <  level_list[level]: 
                        level_list[level].append(root.val)    
                        curr_ans = True 
                    else: 
                        curr_ans = False
                else: 
                    level[level] = [root.val]
                    curr_ans = True 
                right_ans = even_odd(root.right, level+1)
                return left_ans and curr_ans and right_ans
            return True
        return even_odd(root, 0) 