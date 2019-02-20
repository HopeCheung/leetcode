# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root == None:
            return
        
        order = []
        def preorder(root):
            if root != None:
                order.append(root.val)
                preorder(root.left)
                preorder(root.right)
        
        def construct(root, order):
            if len(order) != 0:
                root.right = TreeNode(order[0])
                construct(root.right, order[1:])
                
        preorder(root)
        root.left = None
        construct(root, order[1:])
        
        
        