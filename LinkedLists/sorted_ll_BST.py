# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
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
    def sortedListToBST(self, head):
        def ll_to_arr(head):
            arr = [] 
            while head != None:
                arr.append(head.val)
                head = head.next
            return arr
        def arr_to_BST(arr, l, r):
            if l <= r:
                mid = (l + r) // 2
                root =  TreeNode(
                    val=arr[mid], 
                    left=arr_to_BST(arr, l, mid-1),
                    right=arr_to_BST(arr, mid+1,r)
                )
                return root
            else:
                return None
        arr = ll_to_arr(head)
        return arr_to_BST(arr, 0, len(arr)-1)
if __name__  == "__main__": 
    s = Solution()
    ll = [-10,-3,0,5,9]
    head = MakeLinkedList(ll).head
    print(s.sortedListToBST(head))