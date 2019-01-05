class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        result, sol = [], []
        one_line = ''
        for i in range(n):
            one_line = one_line + '.'
        for j in range(n):
            sol.append(one_line)
        
        def is_valid(row, col, sol):
            if row == 0:
                return True
            for i in range(row):
                if sol[i][col] == 'Q':
                    return False
            
            i, j = row - 1, col - 1
            while i >= 0 and j >= 0:
                if sol[i][j] == 'Q':
                    return False
                i, j = i - 1, j - 1
            i, j = row - 1, col + 1
            while i >= 0 and j < n:
                if sol[i][j] == 'Q':
                    return False
                i, j = i - 1, j + 1
            
            return True
        
        def solve(row, sol):
            if row == n:
                result.append(sol[:])
                return
            for col in range(n):
                if is_valid(row, col, sol):
                    sol[row] = sol[row][0:col] + 'Q' + sol[row][col+1:]
                    solve(row+1, sol)
                    sol[row] = sol[row][0:col] + '.' + sol[row][col+1:]
        solve(0, sol)
        return result
            
        
# ##############---------failure     
        
 
class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        def check(k,j,board):
            for i in range(k):
                if board[i]==j or abs(k-i)==abs(board[i]-j):
                    return False
            return True
        
        def dfs(depth,board,valuelist,solution):
            #for i in range(len(board)):
            if depth==len(board):
                solution.append(valuelist)
            for row in range(len(board)):
                if check(depth,row,board):
                    s='.'*len(board)
                    board[depth]=row
                    dfs(depth+1,board,valuelist+[s[:row]+'Q'+s[row+1:]],solution)
        board=[-1 for i in range(n)]
        solution=[]
        dfs(0,board,[],solution)
        return solution
    

                           
            
                        
            
        
