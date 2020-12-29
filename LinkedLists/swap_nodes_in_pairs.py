class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head): 
        if head == None: 
            return None
        sent = ListNode(next=head)
        curr = head
        while curr.next != None: 
            temp = curr.next.next
            curr.next.next = curr
            curr.next = temp
            curr = temp
        return sent.next
