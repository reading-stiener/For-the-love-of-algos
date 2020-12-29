#User function Template for python3

''' Node for linked list:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''
def parse_util(head, count):
    if head.next is None:
        print(count)
        return count
    else:
        print(count) 
        count += 1
        return parse_util(head.next, count)
def sum_ll(head, count): 
    total = 0
    while head:
        total += head.data * 10**count
        count -= 1
        head = head.next
    return total

def num_to_ll(num):
    prev = None
    while(num>0): 
        curr = Node(num%10)
        curr.next = prev
        prev = curr
        num //= 10
    return curr 
    
def addLists(first, second):
    # code here
    # return head of sum list
    first_count = parse_util(first, 0) 
    second_count = parse_util(second, 0)
    first_sum = sum_ll(first, first_count)
    second_sum = sum_ll(second, second_count)
    sum_total = first_sum + second_sum
    return num_to_ll(sum_total) 
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

# prints the elements of linked list starting with head
def printList(n):
    while n:
        print(n.data,end=' ')
        n = n.next
    print()

if __name__ == '__main__':
    for _ in range(int(input())):
        
        n = int(input())
        arr1 = ( int(x) for x in input().split() )
        LL1 = LinkedList()
        for i in arr1:
            LL1.insert(i)
        
        m = int(input())
        arr2 = ( int(x) for x in input().split() )
        LL2 = LinkedList()
        for i in arr2:
            LL2.insert(i)
        
        res = addLists(LL1.head, LL2.head)
        printList(res)
# } Driver Code Ends