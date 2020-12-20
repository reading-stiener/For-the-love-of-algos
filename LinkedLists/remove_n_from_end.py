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

class Solution:
    def removeNthFromEnd(self, head, n):
        def remove_n_recur(prev, curr, n):
            # end of recursive stack
            if curr.next == None:
                if n == 1:
                    if prev:
                        prev.next = None
                    else:
                        return None
                else: 
                    return 2
            else:
                count = remove_n_recur(curr, curr.next, n)
                if count == n:
                    if prev: 
                        prev.next = curr.next
                        return prev.next
                    else:
                        return curr.next
                elif type(count) == int:
                    print(type(count))
                    return count + 1
                else:
                    return curr
        return remove_n_recur(None, head, n)
  
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
    
if __name__ == "__main__":
    ll = [1,2,3,4,5]
    LL = MakeLinkedList(ll)
    print(LL) 
    s = Solution()
    print(s.removeNthFromEnd(LL.head, 2))
   
