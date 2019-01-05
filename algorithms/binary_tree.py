class Node:
	def __init__(self, key, right, left, p):
		self.key = key
		self.right = right
		self.left = left
		self.parent = parent

class tree:
	def __init__(self):
		self.root = None
		self.size = 0

	def tree_insert(self, insertNode):
		if self.root:
			self.insert(insertode, self.root)
		else:
			self.root = insertNode
		self.size += 1
		return self.root

	def insert(self, insertNode, currrentNode):
		if insertNode.key < currrentNode.key:
			if currrentNode.left:
				self.insert(insertNode, currentNode.left)
			else:
				currrentNode.left = insertNode
		elif insertNode.key > currrentNode.key:
			if currrentNode.right:
				self.insert(insertNode, currentNode.right)
			else:
				currrentNode.right = insertNode

	def inorder(self):
		if self.root != None:
			self.inorder(self.root.left)
			print(self.root.key)
			self.inorder(self.root,right)

	def preorder(self):
		if self.root != None:
			print(self.root.key)
			self.preorder(self.root.left)
			slef.preorder(self.root.right)

	def postorder(self):
		if self.root != None:
			self.preorder(self.root.left)
			slef.preorder(self.root.right)
			print(self.root.key)

	def tree_minumum(self, treeNode):
                while treeNode.left != None:
                        treeNode = treeNode.left
                return treeNode
        
        def tree_maximum(self, treeNode):
                while treeNode.right != None:
                        treeNode = treeNode.right
                return treeNode

        def tree_delete(self, deleteNode):
                if deleteNode.left == None and deleteNode.right == None:
                        if deleteNode.parent:
                                if deleteNode == deleteNode.parent.left:
                                        deleteNode.parent.left = None
                                else:
                                        deleteNode.parent.right = None
                        else:
                                return None
                elif deleteNode.left == None:
                        self.transplant(deleteNode, deleteNode.right)
                elif deleteNode.right == None:
                        self.transplant(deleteNode, deleteNode.left)
                else:
                        newNode =  self.tree_minumum(deletNode.right)
                        if newNode.parent != deleteNode:
                                self.transplant(newNode, newNode.right)
                                newNode.right = deleteNode.right
                                newNode.right.parent = newNode
                        self.transplant(deleteNode, newNode)
                        newNode.left = deleteNode.left
                        newNode.left.parent = newNode

        def transplant(self, currentNode, childNode):
                if currentNode.parent == None:
                        self.root = childNode
                elif currentNode == currentNode.parent.left:
                        currentNode.parent.left = childNode
                else:
                        currentNode.parent.right = childNode

                

	



