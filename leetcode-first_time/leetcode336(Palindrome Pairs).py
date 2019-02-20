class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        if len(words) == 0:
            return []
        
        def palindrome(s):
            return s == s[::-1]
        
        result = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i == j:
                    continue
                if palindrome(words[i] + words[j]):
                    result.append([i,j])
        return result
##-----------------------time exceed
class Solution2(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        # dic, res = {}, []
        # for i in range(len(words)):
        #     dic[words[i]] = i
        dic, res = {word:i for i, word in enumerate(words)}, []
            
        for i in range(len(words)):
            for j in range(len(words[i]) + 1):
                ls, rs = words[i][:j], words[i][j:]
                if rs == rs[::-1] and ls[::-1] in dic and dic[ls[::-1]] != i:
                    res.append([i, dic[ls[::-1]]])
                if j != 0 and ls == ls[::-1] and rs[::-1] in dic and dic[rs[::-1]] != i:
                    res.append([dic[rs[::-1]], i])
        return res
                    
