"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        order = []
        
        def bfs(level, root):
            if root == None:
                return
            if level >= len(order):
                order.append([])
            order[level].append(root.val)
            for child in root.children:
                bfs(level+1, child)
        
        bfs(0, root)
        return order
            