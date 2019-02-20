class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        len1, len2 = len(word1), len(word2)
        if word1 == '':
            return len2
        elif word2 == '':
            return len1 
        
        dp = [[0 for j in range(len2+1)] for i in range(len1+1)]
        dp[0][0] = 0
        for i in range(1, len1+1):
            dp[i][0] = i
        for j in range(1, len2+1):
            dp[0][j] = j
            
        for i in range(1, len1+1):
            for j in range(1, len2+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
        return dp[len1][len2]
            
        