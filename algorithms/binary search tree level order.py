# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        
        queue, order = [], []
        def children(node):
            if node.right == None and node.left == None:
                return []
            elif node.right == None:
                return [node.left]
            elif node.left == None:
                return [node.right]
            else:
                return [node.left, node.right]
            
        def bfs():
            while len(queue) > 0:
                node = queue.pop(0)
                for n in children(node):
                    queue.append(n)
                    order.append(n.val)
                    
        if root != None:
            queue.append(root)
            order.append(root.val)
            bfs()
            
        return order

        