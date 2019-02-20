# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head, target):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        new_head = ListNode(0)
        new_head.next = head
        lst1 = new_head
        lst2, lst3 = lst1.next, lst1.next
        
        while lst2 != None and lst2.val < target:
            lst1, lst2, lst3 = lst1.next, lst2.next, lst3.next
        
        while lst3 != None and lst3.next != None:
            if lst3.next.val >= target:
                lst3 = lst3.next
            else:
                lst1.next, lst3.next = lst3.next, lst3.next.next
                lst1 = lst1.next
                lst1.next = lst2
        head = new_head.next
        return head

        