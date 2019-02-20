# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def is_leaf(root):
            return root.left == None and root.right == None
        
        if root == None or is_leaf(root):
            return 0
        
        def find_left(root):
            if root == None or is_leaf(root):
                return 0
            if root.left and is_leaf(root.left):
                return root.left.val + find_left(root.right)
            else:
                return find_left(root.left) + find_left(root.right)
        
        return find_left(root)
        
        