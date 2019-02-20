"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head == None:
            return None       
        res = []
        
        def helper(head):
            if head == None:
                return 
            res.append(head.val)
            if head.child:
                helper(head.child)
            if head.next:
                helper(head.next)
            return
        
        helper(head)
        new_head = Node(res[0], None, None, None)
        ans = new_head
        for i in range(1, len(res)):
            new_head.next = Node(res[i],new_head, None, None)
            new_head = new_head.next
        return ans
        
                
                
            
        