# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        
        order = []
        def levelorder(root, level):
            if root == None:
                return 
            if level >= len(order):
                order.append([])
            if level % 2 == 0:
                order[level] = order[level] + [root.val]
            else:
                order[level] = [root.val] + order[level]
            levelorder(root.left, level+1)
            levelorder(root.right, level+1)
        levelorder(root, 0)
        return order
        