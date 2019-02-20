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
        if head == None or k == 0:
            return head
        
        length, lst = 0, head
        while lst != None:
            length, lst = length + 1, lst.next   
            
        k1 = k % length
        if k1 == 0:
            return head
        k2 = length - k1
        lst1, lst2, lst4 = head, head, head
        while length > 1:
            if k2 > 1:
                lst2, k2 = lst2.next, k2 - 1
            lst4, length = lst4.next, length - 1
        lst3= lst2.next
        
        #print(lst1.val, lst2.val, lst3.val, lst4.val)
        head = lst3
        lst4.next = lst1
        lst2.next = None
        return head
                
            
        
        
            
        

        