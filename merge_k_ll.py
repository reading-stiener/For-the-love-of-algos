# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self): 
        list_string = ""
        curr = self
        while curr:
            list_string += str(curr.val) + " "
            curr = curr.next
        return list_string
class LinkedList: 
    def __init__(self):
        self.head = None
        self.tail = self.head
    def insert(self, node):
        if not self.head and not self.tail:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
    def __str__(self):
        curr = self.head
        list_string = ""
        while curr:
            list_string += str(curr.val) + " "
            curr = curr.next
        return list_string
def ll(l):
        new_list = LinkedList()
        for val in l:
            new_list.insert(ListNode(val=val))
        print(new_list)
        return new_list.head

import heapq
class Solution:
    def mergeKLists(self, lists):
        node_heap = []
        for curr in lists:
            heapq.heappush(node_heap, (curr.val, id(curr), curr))
        if len(node_heap) < 1:
            return None
        head = ListNode(0)
        curr = head
        while len(node_heap) > 0:
            print(curr.val)
            print(node_heap)
            curr.next = heapq.heappop(node_heap)[2]
            curr = curr.next
            if curr.next:
                heapq.heappush(node_heap, (curr.next.val, id(curr.next), curr.next))
        return head.next

if __name__ == "__main__": 
    s = Solution()
    test1 =  [[1, 2, 2], [1, 1, 2]]
    test_ll = [ll(test_list) for test_list in test1]
    curr = s.mergeKLists(test_ll)
    print(curr)
            