class RBTree(object):
    def __init__(self):
        self.nil = RBTreeNode(0)
        self.root = self.nil

class RBTreeNode(object):
    
    def __init__(self, key, color):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.color = 'R'

class RBTree:

    def __init__(self):
        self.root = None

    def left_rotate(self, node):
        parent = node.parent
        right = node.right

        node.right = right.left
        if node.right:
            node.right.parent = node

        right.left = node
        node.parent = right

        right.parent = parent
        if not parent:
            self.root = right
        else:
            if parent.left == node:
                parent.left = right
            else:
                parent.right = right
        right.color = node.color
        node.color = 'R'

    def right_rotate(self, node):
        parent = node.parent
        left = node.left

        node.left = left.right
        if node.left:
            node.left.parent = node

        left.right = node
        node.parent = left

        left.parent = parent
        if not parent:
            self.root = left
        else:
            if parent.left == node:
                parent.left = left
            else:
                parent.right = left
        left.color = node.color
        node.color = 'R'

    def flipcolor(self, node):
        node.right.color = 'B'
        node.right.color = 'B'
        node.color = 'R'


    def tree_insert(self, insertnode):
        if not self.root:
            self.root = insertnode
            insertnode.color = 'B'
        else:
            self.insert(self.root, insertnode)


    def insert(self, currnode, insertnode):
        if insertnode.key < currnode.key:
            if currnode.left:
                self.insert(currnode.left, insertnode)
            else:
                currnode.left = insertnode
        elif insertnode.key > currnode.key:
            if currnode.right:
                self.insert(currnode.right, insertnode)
            else:
                currnode.right = insertnode
        self.insertfix(currnode)

    def insertfix(self, node):
        if node.right.color === 'R' and node.left.color != 'R':
            self.left_rotate(node)
        if node.left.color == 'R' and node.left.left.color == 'R':
            self.right_rotate(node)
        if node.left.color == 'R' and node.right.color == 'R':
            self.flipcolor(node)
        
        
        
                

    
