# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):
        curr_a, curr_b = headA, headB
        while curr_a != None and curr_b != None:
            curr_a, curr_b = curr_a.next, curr_b.next
        count = 0
        if curr_a == None:
            while curr_b:
                count += 1
                curr_b = curr_b.next
            curr_a, curr_b = headA, headB
            for i in range(count):
                curr_b = curr_b.next
            while curr_a and curr_a != curr_b:
                curr_a, curr_b = curr_a.next, curr_b.next
        else:
            while curr_a:
                count += 1
                curr_a = curr_a.next
            curr_a, curr_b = headA, headB
            for i in range(count):
                curr_a = curr_a.next
            while curr_a and curr_a != curr_b:
                curr_a, curr_b = curr_a.next, curr_b.next
        return curr_a

