class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if len(triangle) == 0:
            return 0
        
        def dfs(triangle, path, position):
            if len(triangle) == 0:
                return path
            elif len(triangle) == 1:
                return dfs(triangle[1:], path + triangle[0][position], position )
            else:
                return min(dfs(triangle[1:], path + triangle[0][position], position), dfs(triangle[1:], path + triangle[0][position], position + 1))
        
        return dfs(triangle, 0, 0)
####--------dfs - time exceeded
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if len(triangle) == 0:
            return 0
        
        dp = triangle[-1]
        
        for i in range(len(triangle)-2, -1, -1):
            for j in range(i+1):
                dp[j] = triangle[i][j] + min(dp[j], dp[j+1])
        
        return dp[0]
##-----------dynamic programing
            

            
        