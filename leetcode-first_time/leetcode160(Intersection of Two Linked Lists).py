# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA == None or headB == None:
            return None
        
        lst1, lst2 = headA, headB
        while lst1.next != None:
            lst1 = lst1.next
        lst1.next = lst2
        
        slow, fast, divide = headA, headA, None
        while slow != None and fast != None and fast.next != None:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                divide = slow
                break
        if divide == None:
            lst1.next = None
            return None
        
        start = headA
        while start != divide:
            start, divide = start.next, divide.next
        lst1.next = None
        return divide
        