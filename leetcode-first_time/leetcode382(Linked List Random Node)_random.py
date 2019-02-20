# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import random
class Solution:

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.lst = head
        self.length = 0
        while head != None:
            self.length, head = self.length + 1, head.next

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        pos = random.randint(0, self.length-1)
        new_head = self.lst
        while pos > 0:
            new_head, pos = new_head.next, pos - 1
        return new_head.val
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()