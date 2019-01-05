# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head == None:
            return head
        
        lst, backup, length = head, [], 0
        while lst != None:
            backup.append(lst)
            lst, length = lst.next, length + 1
        
        i, point4 = length // 2, None
        j = i - 1
        while i != len(backup) - 1:
            point1, point2, point3 = backup[j], backup[i], backup[len(backup)-1]
            point1.next = point2.next
            point3.next = point2
            point2.next = point4
            point4 = point2
            backup.remove(backup[i])
            i = len(backup) // 2
            j = i - 1
##-------time exceeded
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution2(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head == None:
            return 
        
        lst1, lst2 = head, head
        while lst1 != None and lst2 != None and lst2.next != None:
            lst1 = lst1.next
            lst2 = lst2.next.next
        
        head2 = lst1.next
        if head2 == None:
            return
        
        point1, point2, point3 = head2, head2.next, head2
        while point2 != None:
            point1.next = point2.next
            point2.next = point3
            point3 = point2
            point2 = point1.next
        head2 = point3
        lst1.next = head2
        
        head1 = head
        while head1 != lst1 and head2 != None:
            lst1.next = head2.next
            head2.next = head1.next
            head1.next = head2
            head1 = head2.next
            head2 = lst1.next

        
        
            
        
