class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        if endWord not in wordList:
            return []
        wordList.remove(endWord)
        
        def compare(s1, s2):
            return s1 == s2 or len([1 for i in range(len(s1)) if s1[i] != s2[i]]) == 1
        
        result = []
        def helper(begin, end, wordList, one_result):
            if compare(begin, end):
                one_result = one_result + [end]
                result.append(one_result[:])
            else:
                for i in range(len(wordList)):
                    if compare(begin, wordList[i]):
                        one_result.append(wordList[i])
                        helper(wordList[i], end, wordList[:i] + wordList[i+1:], one_result)
                        one_result.pop()
                        
        helper(beginWord, endWord, wordList, [])
        if result == []:
            return []
        length = min([len(elem) for elem in result])
        result = [[beginWord] + elem for elem in result if len(elem) == length]
        return result

######-----time limit
class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        visited = set()
        wordSet = set(wordList)
        
        queue = [(beginWord, 1)]
        
        while len(queue) > 0:
            word, count = queue.pop(0)
            if word == endWord:
                return count
            if word in visited:
                continue
                
            for i in range(len(word)):
                for j in range(0, 26): # try all possible one character permutations
                    char = ord('a') + j
                    changed_word = word[0:i] + chr(char) + word[i + 1:]
                    if changed_word in wordSet: # if permuted word is in word list then add children
                        queue.append((changed_word, count + 1))
            visited.add(word) # mark word as visited
        
        return 0 # if queue is exhausted and code reachers here then its impossible to reach endWord
###--bfs
