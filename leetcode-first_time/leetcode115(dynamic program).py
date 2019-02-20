class Solution:
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        len_s, len_t = len(s), len(t)
        dp = [[0 for j in range(len_t + 1)] for i in range(len_s + 1)] #(dp 一般要多一位)
        dp[0][0] = 1
        for i in range(1, len_s):
            dp[i][0] = 1
        for j in range(1, len_t):
            dp[0][j] = 0                   #根据题意找到初始状态
            
        for i in range(1, len_s+1):
            for j in range(1, len_t+1):
                dp[i][j] = dp[i-1][j] + dp[i-1][j-1] * (s[i-1] == t[j-1])
                #动态方程 最好举例列表找出
        return dp[len_s][len_t]
        
