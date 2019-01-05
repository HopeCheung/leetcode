# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return    
        x = len(nums) // 2
        root = TreeNode(nums[x])
        root.left = self.sortedArrayToBST(nums[:x])
        root.right = self.sortedArrayToBST(nums[x+1:])
        return root

        