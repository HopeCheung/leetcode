class Solution(object):
    def longestPalindrome(self, s):
        if len(s) <= 1:
            return s
        
        dp = [[False for i in range(len(s))] for j in range(len(s))]
        max_len, begin, end = 1, 0, 0
        
        for i in range(len(s)-2, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j] and (j-i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if max_len < j-i+1:
                        max_len = j-i+1
                        begin, end = i, j
        return s[begin:end+1]
                
                

            
        
        