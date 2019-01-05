class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def Level(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        order = []
        
        def level_order(root, level):
            if root == None:
                return
            if len(order) < level + 1:
                order.append([])
            order[level].append(root.val)
            level_order(root.left, level + 1)
            level_order(root.right, level + 1)
        
        level_order(root, 0)      
        ans = max(sum([sum(elem) for elem in order[::2]]), sum([sum(elem) for elem in order[1::2]]))
        return ans