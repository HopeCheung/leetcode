class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def dfs(board, word, i, j, m, n):
            if word == '':
                return True
            if i < 0 or i >= m or j < 0 or j >= n:
                return False
            
            if word[0] == board[i][j]:
                board[i][j] = 0
                res = dfs(board, word[1:], i+1, j, m, n) or dfs(board, word[1:], i-1, j, m, n) or dfs(board, word[1:], i, j+1, m, n) or dfs(board, word[1:], i, j-1, m, n) 
                board[i][j] =word[0]
                return res
            
        if len(word) == 0:
            return True
        
        m, n = len(board), len(board[0])
        if m == 0 or n == 0:
            return False
        
        for i in range(m):
            for j in range(n):
                if dfs(board, word, i, j, m, n):
                    return True
        return False
        
        
        