#leetcode 62
class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0 for j in range(m)] for i in range(n)]
        dp[0][0] = 1
        for j in range(1, m):
            dp[0][j] = 1
        for i in range(1, n):
            dp[i][0] = 1
            
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[n-1][m-1]

#leetcode 63
class Solution2:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        dp = [[0 for j in range(len(obstacleGrid[0]))] for i in range(len(obstacleGrid))]
        dp[0][0] = 1 if obstacleGrid[0][0] != 1 else 0
        for i in range(1, len(obstacleGrid)):
            dp[i][0] = dp[i-1][0] if obstacleGrid[i][0] != 1 else 0
        for j in range(1, len(obstacleGrid[0])):
            dp[0][j] = dp[0][j-1] if obstacleGrid[0][j] != 1 else 0
            
        for i in range(1, len(obstacleGrid)):
            for j in range(1, len(obstacleGrid[0])):
                dp[i][j] = dp[i-1][j] + dp[i][j-1] if obstacleGrid[i][j] != 1 else 0
        
        return dp[len(obstacleGrid)-1][len(obstacleGrid[0])-1]

        