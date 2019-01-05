class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        count = 0
        
        def dfs(m, n):
            nonlocal count
            if m == 0 and n == 0:
                count = count + 1
                return 
            elif n < 0 or m < 0:
                return 
            elif m == 0 and n > 0:
                dfs(m, n-1)
            elif n == 0 and m > 0:
                dfs(m-1, n)
            else:
                dfs(m, n-1)
                dfs(m-1, n)
        
        dfs(m-1, n-1)
        return count
            
######-------------dps: serious time exceeded
class Solution2:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        one_line = [1 for j in range(m)]
        path = [one_line[:] for i in range(n)]
        
        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0:
                    path[i][j] == 1
                else:
                    path[i][j] = path[i-1][j] + path[i][j-1]
        
        return path[i][j]

    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid[0][0] == 1:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                else:
                    if i == 0:
                        if j > 0 and obstacleGrid[i][j-1] == 0:
                            obstacleGrid[i][j] = 0
                        else:
                            obstacleGrid[i][j] = 1
                    elif j == 0:
                        if i> 0 and obstacleGrid[i-1][j] == 0:
                            obstacleGrid[i][j] = 0
                        else:
                            obstacleGrid[i][j] = 1
                    else:
                        obstacleGrid[i][j] = obstacleGrid[i][j-1] + obstacleGrid[i-1][j]
        return obstacleGrid[m-1][n-1]

    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        
        for i in range(m):
            for j in range(n):
                if i > 0 and j > 0:
                    grid[i][j] = grid[i][j] + min(grid[i-1][j], grid[i][j-1])
                elif i == 0 and j > 0:
                    grid[i][j] = grid[i][j] + grid[i][j-1]
                elif j == 0 and i > 0:
                    grid[i][j] = grid[i][j] + grid[i-1][j]
        
        return grid[m-1][n-1]
                    
            
            
            
            
            
