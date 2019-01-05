# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
            return None
        if head.next == None:
            return head
        lst = head
        
        length = 0
        while lst != None:
            lst = lst.next
            length = length + 1
        lst = head
        
        k = k % length
            
        while k > 0:
            new_lst = lst
            while new_lst.next.next != None:
                new_lst = new_lst.next
            lst, lst.next = new_lst.next, lst
            new_lst.next = None
            k = k - 1
        
        head = lst
        return head
        
            
        