class Solution:
    # @param root, a tree node
    # @return a tree node
    def inorder(self, root, lst, listp):
        if root:
            self.inorder(root.left, lst, listp)
            lst.append(root.val); 
            listp.append(root)
            self.inorder(root.right, lst, listp)
            
    def recoverTree(self, root):
        lst, listp = [], []
        self.inorder(root, lst, listp)
        lst.sort()
        for i in range(len(lst)):
            listp[i].val = lst[i]

####-------------inorder
class Solution2:
    # @param root, a tree node
    # @return a tree node
    def FindTwoNodes(self, root):
            if root:
                self.FindTwoNodes(root.left)
                if self.prev and self.prev.val > root.val:
                    self.n2 = root
                    if self.n1 == None: self.n1 = self.prev
                self.prev = root
                self.FindTwoNodes(root.right)
    def recoverTree(self, root):
        self.n1 = self.n2 = None
        self.prev = None
        self.FindTwoNodes(root)
        self.n1.val, self.n2.val = self.n2.val, self.n1.val