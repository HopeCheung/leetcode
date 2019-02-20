# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        
        order = []
        def inorder(root):
            if root != None:
                inorder(root.left)
                order.append(root.val)
                inorder(root.right)
        inorder(root)
        return order

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        
        order = []
        def preorder(root):
            if root != None:
                order.append(root.val)
                preorder(root.left)
                preorder(root.right)
        preorder(root)
        return order

    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        
        order = []
        def postorder(root):
            if root != None:
                postorder(root.left)
                postorder(root.right)
                order.append(root.val)
        postorder(root)
        return order

        