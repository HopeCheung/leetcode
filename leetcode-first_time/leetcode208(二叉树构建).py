class Tree(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Tree('') #注意，初始不能为None， 一定要确定类型，不然出事
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        root = self.root
        def insert_word(word, root):
            if root == None:
                root = Tree(word)
            else:
                if word < root.val:
                    if root.left:
                        insert_word(word, root.left)
                    else:
                        root.left = Tree(word)
                elif word > root.val:
                    if root.right:
                        insert_word(word, root.right)
                    else:
                        root.right = Tree(word)
        insert_word(word, root)
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        root = self.root
        def search_word(word, root):
            if root == None:
                return False
            else:
                if word > root.val:
                    return search_word(word, root.right)
                elif word < root.val:
                    return search_word(word, root.left)
                else:
                    return True
                    
        return search_word(word, root)
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        root = self.root 
        def search_prefix(prefix, root):
            if root == None:
                return False
            else:
                if prefix > root.val:
                    return search_prefix(prefix, root.right)
                elif prefix < root.val:
                    if len(prefix) <= len(root.val) and prefix == root.val[:len(prefix)]:
                        return True
                    return search_prefix(prefix, root.left)
                else:
                    return True
                    
        return search_prefix(prefix, root)

              