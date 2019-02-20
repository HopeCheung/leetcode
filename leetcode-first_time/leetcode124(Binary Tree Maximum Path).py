# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        Solution.maxsum = root.val
        
        def solve(root):
            if root == None:
                return 0
            sum,l,r = root.val,0,0
            if root.left:
                l = solve(root.left)
                if l > 0: 
                    sum += l
            if root.right:
                r = solve(root.right)
                if r > 0: 
                    sum += r
            Solution.maxsum = max(Solution.maxsum,sum)
            return max(root.val,max(root.val + l,root.val+r))
        
        solve(root)
        return Solution.maxsum