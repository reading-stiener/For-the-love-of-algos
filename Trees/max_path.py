# max path in binary tree
# Given a binary tree, find the maximum path sum. The path may start and end at any node in the tree.

import math 
start_val = -math.inf

def max_path(root):
    if not root: 
        return start_val
    print(start_val)
    curr_max = dfs_curr(root, 0, start_val, 0)
    curr_max_left = max_path(root.left)
    curr_max_right = max_path(root.right)
    return max(curr_max, curr_max_left, curr_max_right)    

def dfs_curr(root, path_sum, max_path_val, depth):
    if not root:
        return max_path_val
    else:
        path_sum = path_sum+root.data
        max_path_val = max(path_sum, max_path_val)
        depth += 1
        path_left = dfs_curr(root.left, path_sum, max_path_val, depth)
        path_right = dfs_curr(root.right, path_sum, max_path_val, depth)
        if depth == 1: 
            return max(
            root.data,
            path_left,
            path_right,
            path_right+path_left-root.data
        )
        else: 
            return max(
                root.data,
                path_left,
                path_right
            )


#{ 
#  Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(50000)
#Contributed by Sudarshan Sharma
from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
    
# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root
    
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        print(max_path(root))


# } Driver Code Ends