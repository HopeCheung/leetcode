class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []
        visited = [[True for j in range(len(matrix[0]))] for i in range(len(matrix))]
        
        def is_valid(x, y):
            return x >= 0 and x < len(matrix) and y >= 0 and y < len(matrix[0]) and visited[x][y]
        
        def is_Pacific(x, y):
            return x == 0 or y == 0
        def is_Atlantic(x, y):
            return x == len(matrix) - 1 or y == len(matrix[0]) - 1
        
        res = []
        def helper(x, y, symbol):
            if is_Pacific(x, y):
                symbol.add(1)
            if is_Atlantic(x, y):
                symbol.add(-1)
            if symbol == set([-1, 1]):
                return True
                    
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for d in directions:
                next_x, next_y = x + d[0], y + d[1]
                if is_valid(next_x, next_y) and matrix[next_x][next_y] <= matrix[x][y]:
                    visited[next_x][next_y] = False
                    if helper(next_x, next_y, symbol):
                        visited[next_x][next_y] = True
                        return True
                    visited[next_x][next_y] = True

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                symbol = set()
                visited[i][j] = False
                if helper(i, j, symbol):
                    res.append([i, j])
                visited[i][j] = True
        return res
#------------------------DFS----TLE--------------------------------------------------
class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix: return []
        self.directions = [(1,0),(-1,0),(0,1),(0,-1)]
        m = len(matrix)
        n = len(matrix[0])
        p_visited = [[False for _ in range(n)] for _ in range(m)]
        
        a_visited = [[False for _ in range(n)] for _ in range(m)]
        result = []
        
        for i in range(m):
            # p_visited[i][0] = True
            # a_visited[i][n-1] = True
            self.dfs(matrix, i, 0, p_visited, m, n)
            self.dfs(matrix, i, n-1, a_visited, m, n)
        for j in range(n):
            # p_visited[0][j] = True
            # a_visited[m-1][j] = True
            self.dfs(matrix, 0, j, p_visited, m, n)
            self.dfs(matrix, m-1, j, a_visited, m, n)
            
        for i in range(m):
            for j in range(n):
                if p_visited[i][j] and a_visited[i][j]:
                    result.append([i,j])
        return result
                
                
    def dfs(self, matrix, i, j, visited, m, n):
        # when dfs called, meaning its caller already verified this point 
        visited[i][j] = True
        for dir in self.directions:
            x, y = i + dir[0], j + dir[1]
            if x < 0 or x >= m or y < 0 or y >= n or visited[x][y] or matrix[x][y] < matrix[i][j]:
                continue
            self.dfs(matrix, x, y, visited, m, n)
#----------Better DFS-----------------------------------------------------------------------