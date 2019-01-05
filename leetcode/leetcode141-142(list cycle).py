# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None or head.next == None:
            return False
        
        lst1, lst2 = head.next, head.next.next
        while lst1 != None and lst2 != None and lst2.next != None:
            if lst1 == lst2:
                return True
            else:
                lst1 = lst1.next
                lst2 = lst2.next.next
        return False
##------双指针
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        
        lst1, lst2 = head, head
        while lst1 != None and lst2 != None and lst2.next != None:
            lst1, lst2 = lst1.next, lst2.next.next
            if lst1 == lst2:
                while lst1 != head:
                    lst1, head = lst1.next, head.next
                return head
        return None
##------追击问题。。。