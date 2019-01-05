class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if preorder == [] or inorder == []:
            return None
        root = TreeNode(preorder[0])
        x = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:x+1], inorder[0:x])
        root.right = self.buildTree(preorder[x+1:], inorder[x+1:])
        return root
####------build tree with preorder and inorder

class Solution2:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if inorder == [] or postorder == []:
            return None
        root = TreeNode(postorder[-1])
        x = inorder.index(root.val)
        root.left = self.buildTree(inorder[0:x], postorder[0:x])
        root.right = self.buildTree(inorder[x+1:], postorder[x:-1])
        return root
####------build tree with postorder and inorder
