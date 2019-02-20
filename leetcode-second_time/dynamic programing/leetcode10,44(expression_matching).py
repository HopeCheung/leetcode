#leetcode10
class Solution(object):
    def isMatch(self, text, pattern):
        dp = [[False] * (len(pattern) + 1) for _  in range(len(text) + 1)]

        dp[-1][-1] = True
        for i in range(len(text), -1, -1):
            for j in range(len(pattern) - 1, -1, -1):
                first_match = i < len(text) and pattern[j] in {text[i], '.'}
                if j+1 < len(pattern) and pattern[j+1] == '*':
                    dp[i][j] = dp[i][j+2] or (first_match and dp[i+1][j])
                else:
                    dp[i][j] = first_match and dp[i+1][j+1]

        return dp[0][0]
#leetcode44
class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [[False for j in range(len(s)+1)] for i in range(len(p)+1)]
        dp[-1][-1] = True
        
        for i in range(len(p)-1, -1, -1):
            for j in range(len(s), -1, -1):
                if p[i] == "*":
                    dp[i][j] = dp[i+1][j] or (j+1 <= len(s) and (dp[i][j+1] or dp[i+1][j+1])) 
                else:
                    dp[i][j] = ((j+1 <= len(s)) and dp[i+1][j+1]) and (p[i] == s[j] or p[i] == "?")
        
        return dp[0][0]
        