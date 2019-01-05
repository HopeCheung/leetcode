class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0:
            return 0
        
        def check(matrix, x, y, edge):
            if x + edge > len(matrix) or y + edge > len(matrix[0]):
                return False
            for i in range(x, x+edge):
                for j in range(y, y+edge):
                    if matrix[i][j] == '0':
                        return False
            return True
        
        def dfs(matrix, x, y, edge):
            if check(matrix, x, y, edge):
                return dfs(matrix, x, y, edge+1)
            else:
                return edge - 1
        
        area = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '1':
                    area = max(area, pow(dfs(matrix, i, j, 1), 2))
        return area
##-----slow dps
class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0:
            return 0
        
        dp = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]
        area = 0
        for i in range(len(matrix)):
            dp[i][0] = int(matrix[i][0])
            area = max(area, dp[i][0])
        for j in range(len(matrix[0])):
            dp[0][j] = int(matrix[0][j])
            area = max(area, dp[0][j])
            
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j-1], min(dp[i-1][j], dp[i][j-1])) + 1
                    area = max(area, dp[i][j] * dp[i][j])
        return area
            
###----fasr--dynamic programing