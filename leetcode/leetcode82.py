# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        
        lst = head
        if lst.val != lst.next.val:
            lst2 = lst.next
        else:
            while lst != None and lst.next != None and lst.val == lst.next.val:
                while lst != None and lst.next != None and lst.val == lst.next.val:
                    lst = lst.next
                lst = lst.next
            if lst == None:
                return None
            head, lst2 = lst, lst.next
            
        while lst2 != None and lst2.next != None:
            if lst2.val != lst2.next.val:
                lst.next = lst2
                lst, lst2 = lst.next, lst2.next
            else:
                while lst2 != None and lst2.next != None and lst2.val == lst2.next.val:
                    lst2 = lst2.next
                lst2 = lst2.next
        lst.next = lst2        
        return head           
#################------------slow