#User function Template for python3

'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
'''
def compare(head1, head2):
    #return 1/-1/0

    while head1 or head2:
        if not head1 and head2:
            return -1
        elif not head2 and head1:
            return 1
        elif head1.data != head2.data: 
            if head1.data > head2.data:
                return 1
            else: 
                return -1
        else: 
            head1 = head1.next
            head2 = head2.next
            
    return 0

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Llist:
    def __init__(self):
        self.head=None
    
    def insert(self,data,tail):
        node=Node(data)
        
        if not self.head:
            self.head=node
            return node
        
        tail.next=node
        return node
        

        
    

        
def printList(head):
    while head:
        print(head.data,end=' ')
        head=head.next
        
if __name__ == '__main__':
    t=int(input())
    
    for tcs in range(t):
        
        n1=int(input())
        arr1=input().split()
        ll1=Llist()
        tail=None
        for nodeData in arr1:
            tail=ll1.insert(nodeData,tail)
            
            
        n2=int(input())
        arr2=input().split()
        ll2=Llist()
        tail=None
        for nodeData in arr2:
            tail=ll2.insert(nodeData,tail)
        
        
        print(compare(ll1.head,ll2.head))
        
    
    
# } Driver Code Ends