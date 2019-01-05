# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return 
         
        def contain(root, node):
            if root == None:
                return False
            elif root == node:
                return True
            elif node.val < root.val:
                return contain(root.left, node)
            elif node.val > root.val:
                return contain(root.right, node)
            
        def helper(root, p, q):
            if root == None:
                return
            elif contain(root.left, p) and contain(root.right, q):
                return root
            else:
                return helper(root.left, p, q) or helper(root.right, p, q)
            
        if contain(p, q):
            return p
        elif contain(q, p):
            return q
        else:
            if p.val < q.val:
                return helper(root, p, q)
            else:
                return helper(root, q, p)
###-------------binary-search-tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution2:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return 
        
        def contain(root, node):
            if root == None:
                return False
            elif root == node:
                return True
            else:
                return contain(root.left, node) or contain(root.right, node)
            
        def helper(root, p, q):
            if root == None:
                return
            elif (contain(root.left, p) and contain(root.right, q)) or (contain(root.left, q) and contain(root.right, p)):
                return root
            else:
                return helper(root.left, p, q) or helper(root.right, p, q)
        
        if contain(p, q):
            return p
        elif contain(q, p):
            return q
        else:
            return helper(root, p, q)
###------------- binary tree
            
        
