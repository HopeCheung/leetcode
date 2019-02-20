class Solution:
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [float("inf")] * n
        dp[0] = 0
        
        for i in range(1, n):
            for j in range(i):
                if (j+1 == (i+1) // 2 and (i+1) % 2 == 0) or j+1 == i:
                    mid  = dp[j] + 1
                else:
                    mid = float("inf")
                dp[i] = min(dp[i], mid)
        return dp[n-1]
#------------DP-----TLE------------------------------------------------
class Solution:
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0
        elif n % 2 == 0:
            return 1 + self.integerReplacement(n//2)
        else:
            return 1 + min(self.integerReplacement(n+1),self.integerReplacement(n-1))
            
    
        