# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head == None:
            return None
        
        length = 0
        lst = head 
        while lst != None:
            length, lst = length + 1, lst.next
        n = length - n
        
        if n == 0:
            return head.next
        first, second = head, head.next

        while n-1 > 0:
            first, second = first.next, second.next
            n = n - 1
        first.next = second.next
        second.next = None
        return head

        
            