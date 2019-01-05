# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None:
            return False  

        def judge(root, sum):
            if root == None and sum != 0:
                return False
            if root.left == None and root.right == None and root.val == sum:
                return True
            elif root.left == None and root.right != None:
                return judge(root.right, sum - root.val)
            elif root.left != None and root.right == None:
                return judge(root.left, sum - root.val)
            return judge(root.left, sum - root.val) or judge(root.right, sum - root.val)
            
        return judge(root, sum)
        
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        
        result = []
        def add_path(root, sum, path):
            if root == None and sum != 0:
                return 
            if root.left == None and root.right == None and root.val == sum:
                path = path + [root.val]
                result.append(path)
                return 
            elif root.left == None and root.right != None:
                add_path(root.right, sum - root.val, path + [root.val])
            elif root.left != None and root.right == None:
                add_path(root.left, sum -  root.val, path + [root.val])
            else:
                add_path(root.left, sum - root.val, path + [root.val])
                add_path(root.right, sum - root.val, path + [root.val])
        
        add_path(root, sum, [])
        return result
        