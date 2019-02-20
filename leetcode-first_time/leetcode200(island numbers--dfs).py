class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0
        
        def check(x, y):
            if x in range(0, len(grid)) and y in range(0, len(grid[0])) and grid[x][y] == '1' and visited[x][y] == False:
                return True
            
        def dfs(x, y):
            n_row, n_col = [1,0,-1,0], [0,1,0,-1]
            for k in range(4):
                next_x, next_y = x + n_row[k], y + n_col[k]
                if check(next_x, next_y):
                    visited[next_x][next_y] = True
                    dfs(next_x, next_y)
        
        visited = [[False for j in range(len(grid[0]))] for i in range(len(grid))]
        count = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if check(x, y):
                    visited[x][y] = True
                    dfs(x, y)
                    count = count + 1
        return count
        
        
        