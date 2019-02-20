class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if wordDict == []:
            return False
        if s == '':
            return True
        
        dp = [True] + len(s) * [False]
        for i in range(len(s)):
            for j in range(i+1):
                if dp[j] and s[j:i+1] in wordDict:
                    dp[i+1] = True
                    break
        return dp[len(s)]
####-----dynamic programing
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        if wordDict == [] or s == '':
            return []
        
        result = []
        def helper(s, curr_s, wordDict, one_result):
            if curr_s == s:
                result.append(one_result[1:])
            else:
                for word in wordDict:
                    if curr_s + word in s:
                        helper(s, curr_s+word, wordDict, one_result+' '+word)
                return 
            
        helper(s, '', wordDict, '')
        return result
###-------dfs time exceeded