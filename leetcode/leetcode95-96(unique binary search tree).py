class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def dfs(left, right):
            if left > right:
                return [None]
            res = []
            for i in range(left, right + 1):
                leftNode = dfs(left, i-1)
                rightNode = dfs(i+1, right)
                for l in leftNode:
                    for r in rightNode:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        res.append(root)
            return res
                        
        if n == 0:
            return []
        return dfs(1, n)

    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return n
        
        backpack = {0:0, 1:1}
        
        i = 2
        while i <= n:
            curr = 0
            for j in range(1, i+1):
                if backpack[j-1] == 0 or backpack[i-j] == 0:
                    curr = curr + max(backpack[i-j], backpack[j-1])
                else:
                    curr = curr + backpack[j-1] * backpack[i-j]
            backpack[i] = curr
            i = i + 1
            
        return backpack[len(backpack)-1]

