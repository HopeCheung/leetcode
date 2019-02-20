# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        
        def left_depth(root):
            if root.left == None:
                return 1
            else:
                return 1 + left_depth(root.left)
        
        def right_depth(root):
            if root.right == None:
                return 1
            else:
                return 1 + right_depth(root.right)
            
        left, right = left_depth(root), right_depth(root)
        if left == right:
            return pow(2, left) - 1
        else:
            return self.countNodes(root.left) + self.countNodes(root.right) + 1