# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        def reverse_ll(head):
            curr = head
            next_curr = curr.next
            curr.next = None
            while next_curr:
                #print(curr.val)
                temp = next_curr.next
                next_curr.next = curr
                curr = next_curr
                next_curr = temp
            return curr
        def add(l1, l2):
            curr_1, curr_2 = l1, l2
            carry = 0
            buff = ListNode()
            curr = buff
            while curr_1 or curr_2:
                if curr_1 and curr_2:
                    tot = curr_1.val + curr_2.val + carry
                    curr.next = ListNode(tot%10)
                    curr = curr.next
                    carry = tot // 10
                    curr_1, curr_2 = curr_1.next, curr_2.next
                elif curr_1:
                    tot = curr_1.val + carry
                    curr.next = ListNode(tot%10)
                    curr = curr.next
                    carry = tot // 10
                    curr_1 = curr_1.next
                else:
                    tot = curr_2.val + carry
                    curr.next = ListNode(tot%10)
                    curr = curr.next
                    carry = tot // 10
                    curr_2 = curr_2.next
            if carry > 0:
                curr.next = ListNode(carry)    
            return reverse_ll(buff.next)
        return add(reverse_ll(l1), reverse_ll(l2))