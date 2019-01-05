# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        
        def judge(root, min_val, max_val):
            if root == None:
                return True
            if min_val != None and root.val <= min_val:
                return False
            if max_val != None and root.val >= max_val:
                return False
            return judge(root.left, min_val, root.val) and judge(root.right, root.val, max_val)
        
        return judge(root, None, None)
##-----------Slow

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solutio2:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        
        result = []
        def inorder(root):
            if root != None:
                inorder(root.left)
                result.append(root.val)
                inorder(root.right)
            else:
                return
        inorder(root)
        return result == sorted(result) and len(result) == len(set(result))
#--------inorder solution