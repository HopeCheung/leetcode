# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root == None:
            return True
        result = []
        
        def insert(root, val):
            if root == None:
                root = TreeNode(val)
            else:
                if val < root.val:
                    if root.left != None:
                        insert(root.left, val)
                    else:
                        root.left = TreeNode(val)
                else:
                    if root.right != None:
                        insert(root.right, val)
                    else:
                        root.right = TreeNode(val)
    
        def order(root):
            if root != None:
                order(root.left)
                result.append(root.val)
                order(root.right)
            else:
                return
        order(root)
        
        result.sort()
        new_root = None
        for val in result:
            insert(new_root, val)
            
        root = new_root
    
            
        
            
        
        