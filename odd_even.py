class Solution:
    ### Could only think of brute force... 
    ### Need understand the stack approach
    def oddEvenJumps(self, A):
        def is_good(A, i):
            step_count = 1
            search = 

        n = len(A)
        count = 0
        for i in range(n): 
            if is_good(A, i): 
                count += 1
        return count