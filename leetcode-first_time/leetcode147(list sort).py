# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        
        head1, head2, head3 = head, head.next, head
        while head2 != None:
            if head2.val >= head3.val:
                head3 = head3.next
                head2 = head2.next
            elif head.val > head2.val:
                head3.next = head2.next
                head2.next = head1
                head, head1 = head2, head2
                head2 = head3.next
            else:
                headn = head1.next
                while headn != head3 and  headn.val < head2.val:
                    headn = headn.next
                    head1 = head1.next
                head3.next = head2.next
                head1.next = head2
                head2.next = headn
                head1 = head
                head2 = head3.next
        
        return head
#----insertion sort
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def merge(left, right):
            lhead, rhead = left, right
            new_lst = ListNode(0)
            head = new_lst
            while lhead and rhead:
                if lhead.val < rhead.val:
                    new_lst.next = lhead
                    lhead = lhead.next
                else:
                    new_lst.next = rhead
                    rhead = rhead.next
                new_lst = new_lst.next
            if lhead:
                new_lst.next = lhead
            if rhead:
                new_lst.next = rhead
            return head.next
                
        
        def divided(head):
            if head == None:
                return head
            fast, slow = head, head
            while fast.next != None and fast.next.next != None:
                slow, fast = slow.next, fast.next.next
            return slow
        
        if head is None or head.next is None:
            return head      
        mid = divided(head)
        left, right = head, mid.next
        mid.next = None
        return merge(self.sortList(left),self.sortList(right))
###----merge sort