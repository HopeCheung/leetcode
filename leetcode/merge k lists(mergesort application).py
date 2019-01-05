# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        def mergeTwo(l1, l2):
            if l1 is None:
                return l2
            elif l2 is None:
                return l1
            else:
                if l1.val > l2.val:
                    lst = ListNode(l2.val)
                    lst.next = mergeTwo(l1, l2.next)
                else:
                    lst = ListNode(l1.val)
                    lst.next = mergeTwo(l1.next, l2)
            return lst
        
        def divide(lists):
            if len(lists) == 1:
                return lists[0]
            elif len(lists) == 2:
                return mergeTwo(lists[0], lists[1])
            else:
                left = lists[0 : len(lists)//2]
                right = lists[len(lists)//2 : len(lists)]
                return mergeTwo(divide(left), divide(right))
        
        if len(lists) == 0:
            return None
        return divide(lists)
        
                
        
        
        
        