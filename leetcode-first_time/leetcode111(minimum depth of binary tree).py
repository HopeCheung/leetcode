# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        
        def height(root):
            if root == None:
                return 0
            if root.left == None:
                return height(root.right) + 1
            elif root.right == None:
                return height(root.left) + 1
            return min(height(root.left), height(root.right)) + 1
        
        return height(root)
        