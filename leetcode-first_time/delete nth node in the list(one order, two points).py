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
        new_lst = ListNode(0)
        new_lst.next = head
        first = new_lst
        second = new_lst
        
        #the gap bewteen first and second node is n
        while n >= 0:
            first = first.next
            n = n - 1
            
        while first != None:
            first = first.next
            second = second.next
        if second.next != None:
            second.next = second.next.next
        else:
            return
        return new_lst.next
        
        
        