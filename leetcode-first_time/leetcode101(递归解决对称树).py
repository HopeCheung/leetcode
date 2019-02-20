# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        
        def helper(l, r):
            if l == None and r == None:
                return True
            elif l != None and r != None and l.val == r.val:
                return helper(l.left, r.right) and helper(l.right, r.left)
            else:
                return False
            
        return helper(root.left, root.right)
            
        