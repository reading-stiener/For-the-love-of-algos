class Solution:
    def asteroidCollision(self, asteroids):
        ast_stack = []
        for ast in asteroids:
            if ast > 0:
                ast_dir = 1
            else:
                ast_dir = -1
            if len(ast_stack) == 0:
                stack_dir = ast_dir
                ast_stack.append(ast)
            elif stack_dir == ast_dir or (stack_dir < 0 and ast_dir > 0):
                ast_stack.append(ast)
                stack_dir = ast_dir
            else:
                while len(ast_stack) > 0 and abs(ast) > abs(ast_stack[-1])  and ast_stack[-1] > 0:
                    #print("popped")
                    ast_stack.pop()
                if len(ast_stack) == 0:
                    ast_stack.append(ast)
                    stack_dir = ast_dir
                else:
                    #print(ast_stack[-1])
                    if ast_stack[-1] < 0:
                        ast_stack.append(ast)
                        stack_dir = ast_dir    
                    elif abs(ast) == abs(ast_stack[-1]):
                        ast_stack.pop()
            #print(ast_dir, stack_dir)
        return ast_stack

