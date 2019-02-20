class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0 or s[0] == '0':
            return 0
        
        dp = [0] * (len(s) + 1)
        dp[0], dp[1] = 1, 1
        
        for i in range(2, len(s)+1):
            if int(s[i-2:i]) in range(10, 27) and s[i-1] != "0":
                dp[i] = dp[i-1] + dp[i-2]
            elif int(s[i-2:i]) == 10 or int(s[i-2:i]) == 20:
                dp[i] = dp[i-2]
            elif s[i-1] != "0":
                dp[i] = dp[i-1]
            else:
                return 0
        return dp[len(s)]

        
        