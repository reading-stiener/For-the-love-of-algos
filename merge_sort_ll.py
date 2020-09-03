#User function Template for python3
import math 
def length(head): 
    count = 0
    curr = head
    while curr:
        count += 1
        curr = curr.next
    return count
    
def split_list(head, length):
    printList(head)
    half = length // 2 
    print(half)
    count = 1 
    head_left = head
    head_right = None
    curr = head
    while count < half and curr: 
        curr = curr.next
        count += 1
    head_right = curr.next
    curr.next = None
    return  (head_left, head_right)

def merge(head1, head2):
    print('Merge starts')
    head = None
    if not head1:
        return head2
    if not head2:
        return head1

    if head1.data <= head2.data: 
        head = head1
        head1 = head1.next
    else: 
        head = head2
        head2 = head2.next
    
    curr = head
    while head1 or head2:
        if head1 and head2: 
            if head1.data <= head2.data:
                curr.next = head1
                head1 = head1.next
            else: 
                curr.next = head2
                head2 = head2.next
        elif head1: 
            curr.next = head1
            head1 = head1.next
        else: 
            curr.next = head2
            head2 = head2.next

        curr = curr.next
    return head

def mergeSort(head):
    '''
    :param head: head of unsorted linked list 
    :return: head of sorted linkd list
    
    # Node Class
    class Node:
        def __init__(self, data):  # data -> value stored in node
            self.data = data
            self.next = None
    '''
    if head: 
        len = length(head)
        if len == 1: 
            return head

        head_left, head_right = split_list(head, len)
        printList(head_left)
        printList(head_right)
      
        head_left = mergeSort(head_left)
        head_right = mergeSort(head_right)
        head = merge(head_left, head_right) 
    return head
#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

# Node Class
class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None


# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node    
            return
        self.tail.next = new_node
        self.tail = new_node

# prints the elements of linked list starting with head
def printList(head):
    if head is None:
        print(' ')
        return
    curr_node = head
    while curr_node:
        print(curr_node.data,end=" ")
        curr_node=curr_node.next
    print(' ')


if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        n = int(input())
        p = LinkedList() # create a new linked list 'a'.
        nodes_p = list(map(int, input().strip().split()))
        for x in nodes_p:
            p.append(x)  # add to the end of the list

        printList(mergeSort(p.head))

# } Driver Code Ends