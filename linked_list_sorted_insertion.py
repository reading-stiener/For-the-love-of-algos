#User function Template for python3

def sortedInsert(head1,key):
    # code here
    # return head of edited linked list
    
    cur = head1
    new_node = Node(key)
    
    if not cur:
        head1 = new_node
        return head1
    
    elif key <= cur.data: 
        new_node.next = head1
        head1 = new_node
        return head1
    
    else: 
        while cur.next and key > cur.next.data:
            cur = cur.next
            
    if cur.next: 
        temp = cur.next
        cur.next = new_node
        new_node.next = temp
    else: 
        cur.next = new_node
        
    
    return head1 



#{ 
#  Driver Code Starts
#Initial Template for Python 3

# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        
# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.prev=self.head
    
    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.prev = self.head
        else:
            self.prev.next = new_node
            self.prev = self.prev.next

def printList(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        
        a = LinkedList()
        nodes = list(map(int, input().strip().split()))
        for x in nodes:
            a.append(x)
        
        key=int(input())
        h=sortedInsert(a.head,key)
        printList(h)

# } Driver Code Ends