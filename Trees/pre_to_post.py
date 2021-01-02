import math

# O(nlogn) solution 
def pre_ord_to_post(arr):
    if len(arr) == 0:
        return None
    if len(arr) == 1:
        return Node(arr[0])
    else: 
        root = Node(arr[0])
    for i in range(1, len(arr)):
        new_node = Node(arr[i])
        print('new node', new_node)
        add_BST(root, new_node)
  
    return post_ord(root)

def add_BST(root, new_node):
    if new_node.data <= root.data: 
        if root.left:
            add_BST(root.left, new_node)
        else: 
            root.left = new_node
    else: 
        if root.right:
            add_BST(root.right, new_node)
        else: 
            root.right = new_node

def post_ord(root):
    if root: 
        post_ord(root.left)
        post_ord(root.right)
        print(root.data, end=' ')

def preord_BST_eff(arr):
    min_lim = -math.inf
    max_lim = math.inf

    if len(arr) == 0:
        return None
    elif len(arr) == 1: 
        return Node(arr[0])
    else:
        return pre_BST(arr, 0,  min_lim, max_lim)

# O(n) solution. Took help from geek for geeks
def pre_BST(arr, arr_idx, min_lim, max_lim):
    # base case I 
    if arr_idx >= len(arr):
        print("Base case happened")
        return None
    
    root = None
    print(arr_idx, arr[arr_idx])
    print(min_lim, max_lim)
    if arr[arr_idx] > min_lim and arr[arr_idx] < max_lim:
        root = Node(arr[arr_idx])
        arr_idx += 1

        if arr_idx < len(arr):
            root.right = pre_BST(arr, arr_idx, root.data, max_lim)
            root.left = pre_BST(arr, arr_idx, min_lim, root.data)
            
    return root

def pre_to_post(arr):
    bst = preord_BST_eff(arr)
    post_ord(bst)

class Node: 
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        #pre_ord_to_post(arr)
        pre_to_post(arr)