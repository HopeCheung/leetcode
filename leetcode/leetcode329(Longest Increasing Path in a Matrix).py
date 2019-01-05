class Solution:
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        
        res = []
        def dfs(matrix, x, y, path):
            dirt = [(0,1), (0,-1), (1, 0), (-1,0)]
            for k in range(4):
                next_x, next_y = x + dirt[k][0], y + dirt[k][1]
                if next_x in range(0, len(matrix)) and next_y in range(0, len(matrix[0])) and matrix[next_x][next_y] > matrix[x][y]:
                    if not visited[next_x][next_y]:
                        visited[next_x][next_y] = True
                        dfs(matrix, next_x, next_y, path + 1)
                        visited[next_x][next_y] = False
            else:
                res.append(path)
                return
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                visited = [[False for i in range(len(matrix[0]))] for j in range(len(matrix))]
                dfs(matrix, i, j, 1)
        return max(res)      
######------------------------DFS time exceeded-------------
class Solution:
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        def dfs(x, y):
            if not dp[x][y]:
                curr = matrix[x][y]
                dp[x][y] = 1 + max(
                    dfs(x-1, y) if x - 1 >= 0 and curr > matrix[x-1][y] else 0,
                    dfs(x+1, y) if x + 1 < len(matrix) and curr > matrix[x+1][y] else 0,
                    dfs(x, y-1) if y - 1 >= 0 and curr > matrix[x][y-1] else 0,
                    dfs(x, y+1) if y + 1 < len(matrix[0]) and curr > matrix[x][y+1] else 0
                )
            return dp[x][y]
        
        dp = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]
        return max(dfs(i, j) for i in range(len(matrix)) for j in range(len(matrix[0])))
###-------DFS with DP
    

    
    
        
    

        
