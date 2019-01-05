from collections import defaultdict

class TrieNode(object):
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_leaf = False

class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        curr = self.root
        for char in word:
            curr = curr.children[char]
        curr.is_leaf = True
        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.word_search(word, self.root)
    
    def word_search(self, word, node):
        if len(word) == 0:
            return node.is_leaf
        first = word[0]
        if first == '.':
            for char in node.children:
                if self.word_search(word[1:], node.children[char]):
                    return True
        else:
            if first not in node.children:
                return False
            return self.word_search(word[1:], node.children[first])
        return False
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)