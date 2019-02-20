class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0
        
        dp = [[0 for i in range(n+1)] for j in range(n+1)]
            
        for start in range(1, n+1):
            for j in range(start, n+1):
                i = j - start
                dp[i][j] = min(i + dp[i+1][j], j + dp[i][j-1])
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], k + max(dp[i][k-1], dp[k+1][j]))
        return dp[1][n]
    
    

            
                