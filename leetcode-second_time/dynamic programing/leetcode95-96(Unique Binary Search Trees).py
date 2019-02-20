#leetcode95
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        
        def dfs(left, right):
            if left > right:
                return [None]
            res = []
            for i in range(left, right+1):
                l = dfs(left, i-1)
                r = dfs(i+1, right)
                for j in l:
                    for k in r:
                        root = TreeNode(i)
                        root.left = j
                        root.right = k
                        res.append(root)
            return res
        
        return dfs(1, n)               

#leetcode 96
class Solution2:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return n
        
        dp = [0] * (n+1)
        dp[0], dp[1] = 0, 1
        
        for i in range(2, n+1):
            for j in range(i):
                if i - j - 1 == 0 or j == 0:
                    dp[i] = dp[i] + max(dp[j], dp[i-j-1])
                else:
                    dp[i] = dp[i] + dp[i-j-1] * dp[j]
        return dp[n]

