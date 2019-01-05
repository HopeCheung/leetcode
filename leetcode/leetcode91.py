class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s[0] == '0':
            return 0
        if len(s) == 1:
            return 1
        
        result = []
        def dfs(s, left):
            if left == 0:
                result.append(1)
                return 
            if s == '0':
                return
            elif len(s) == 1:
                dfs(s[1:], left-1)
                return
            else:
                if s[0] == '0':
                    return
                else:
                    dfs(s[1:], left-1)
                    if int(s[0:2]) <= 26 :
                        dfs(s[2:], left-2)
                return
        dfs(s, len(s))
        return len(result)
#---------------------------dfs -----time exceeded

class Solution2:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0 or s[0] == '0':
            return 0
        dp = [1,1]
        
        for i in range(2, len(s)+1):
            if int(s[i-2:i]) in range(10, 27) and s[i-1] != '0':
                dp.append(dp[i-1]+dp[i-2])
            elif int(s[i-2:i]) == 10 or int(s[i-2:i]) == 20:
                dp.append(dp[i-2])
            elif s[i-1] != '0':
                dp.append(dp[i-1])
            else:
                return 0
        return dp[len(s)]
#------------动态规划
