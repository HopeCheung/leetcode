# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        
        def Height(root, level):
            if root == None:
                return level
            return max(Height(root.left, level + 1), Height(root.right, level + 1))
        
        if abs(Height(root.left, 0) - Height(root.right, 0)) < 2:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False