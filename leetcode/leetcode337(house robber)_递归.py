# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def keep_rob(flag, root):
            if root == None:
                return 0
            if flag == 1:
                return max(root.val + keep_rob(0, root.left) + keep_rob(0, root.right), keep_rob(1, root.left) + keep_rob(1, root.right))
            else:
                return keep_rob(1, root.left) + keep_rob(1, root.right)
        
        return keep_rob(1, root)


class Solution2:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def keep_rob(root):
            ret = [0, 0]
            if root == None:
                return ret
            left = keep_rob(root.left)
            right = keep_rob(root.right)
            
            ret[0] = max(left[0], left[1]) + max(right[0], right[1])
            ret[1] = root.val + left[0] + right[0]
            
            return ret