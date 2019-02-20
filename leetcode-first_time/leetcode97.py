class Solution:
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        def dfs(s1, s2, s3):
            if len(s1) + len(s2) != len(s3):
                return False
            elif len(s3) == 0:
                return True
            elif len(s1) != 0 and s1[0] == s3[0] and len(s2) != 0 and s2[0] == s3[0]:
                return dfs(s1[1:], s2, s3[1:]) or dfs(s1, s2[1:], s3[1:])
            elif len(s1) != 0 and s1[0] == s3[0]:
                return dfs(s1[1:], s2, s3[1:])
            elif len(s2) != 0 and s2[0] == s3[0]:
                return dfs(s1, s2[1:], s3[1:])
            else:
                return False
            
        return dfs(s1, s2, s3)
                
###########------------time limit
class Solution2:
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) + len(s2) != len(s3):
            return False
        if len(s1) == 0 and len(s2) == 0 and len(s3) == 0:
            return True
        
        len1, len2 = len(s1), len(s2)
        dp = [[0 for j in range(len2+1)] for i in range(len1+1)]
        dp[0][0] = 1
        
        for i in range(1, len1 + 1):
            if s1[i-1] == s3[i-1]:
                dp[i][0] = dp[i-1][0]
        for j in range(1, len2 + 1):
            if s2[j-1] == s3[j-1]:
                dp[0][j] = dp[0][j-1]
        
        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                if s1[i-1] == s3[i+j-1] and dp[i-1][j] == 1:
                    dp[i][j] = dp[i-1][j]
                if s2[j-1] == s3[i+j-1] and dp[i][j-1] == 1:
                    dp[i][j] = dp[i][j-1]
        return dp[len1][len2] == 1
                
