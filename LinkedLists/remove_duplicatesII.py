# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        list_str = ""
        curr = self
        while curr != None:
            list_str += str(curr.val) + " "
            curr = curr.next
        return list_str
class MakeLinkedList:
    def __init__(self, llist):
        self.head = self.make_LL(llist)

    def make_LL(self, llist):
        head = ListNode(val=llist[0])
        curr = head
        for i in range(1,len(llist)):
            curr.next = ListNode(val=llist[i])
            curr = curr.next
        return head
    
    def __str__(self):
        list_str = ""
        curr = self.head
        while curr != None:
            list_str += str(curr.val) + " "
            curr = curr.next
        return list_str
        
class Solution:
    def deleteDuplicatesII(self, head):
        prev = ListNode(None)
        prev.next = head
        first, second = head, head
        head_found = False
        while first != None:
            repeat = False
            while second.next != None and second.next.val == first.val:
                repeat = True
                second = second.next
            if repeat:
                if second.next: 
                    first = second.next
                    second = first
                    prev.next = first
                else:
                    first = prev
                    first.next = None
            else:
                prev = first 
                first = first.next
                second = first
                if not head_found:
                        head_found = True
                        head = prev
        if prev.val == None: 
            return None
        return head
    def deleteDuplicates(self, head):
        curr = head
        while curr != None: 
            if curr.next and curr.next.val == curr.val:
                dup = curr
                while dup.next and dup.next.val == dup.val:
                    dup = dup.next
                curr.next = dup.next
            curr = curr.next
        return head 

if __name__ == "__main__":
    s = Solution()
    ll = [1,1]
    head = MakeLinkedList(ll).head
    new_head = s.deleteDuplicates(head)
    print(new_head)


