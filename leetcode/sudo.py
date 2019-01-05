class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        def judge(lst):
            new_lst = [k for k in lst if k != '.']
            length = len(new_lst)
            return not length == len(set(new_lst))
        
        for elem in board:
            if judge(elem):
                return False
        
        for i in range(9):
            path = []
            for elem in board:
                path += [elem[i]]
            if judge(path):
                return False
        
        for k in range(9):
            path = []
            for r in range(3):
                for c in range(3):
                    path += board[(k//3)*3 + r][(k%3)*3 + c]
            if judge(path):
                return False
        
        return True



    def solveSudoku(self, board):
        def isvaild(i,j):
            for m in range(9):
                if m!=i and board[m][j]==board[i][j]:
                    return False
            for n in range(9):
                if n!=j and board[i][n]==board[i][j]:
                    return False
            for m in range(i//3*3, i//3*3+3):
                for n in range(j//3*3, j//3*3+3):
                    if m!=i and n!=j and board[m][n]==board[i][j]:
                        return False
            return True
        for i in range(9):
            for j in range(9):
                if board[i][j]=='.':
                    for c in '123456789':
                        board[i][j]=c
                        if isvaild(i,j):
                            if self.solveSudoku(board):
                                return True
                            else:
                                board[i][j] = '.'
                        else:
                            board[i][j] = '.'
                    return False
        return True

class Solution2():
	def solveSudo(board):
		dfs(board, 0, 0)
	def is_valid(x, y, board, k):
		for i in range(9):
			if i != x and board[i][y] == k:
				return False
			if i != y and board[x][i] == k:
				return False
		for i in range(x//3*3, x//3*3+3):
			for j in range(y//3*3, y//3*3+3):
				if x != i and y != j and borad[i][j] == k:
					return False
		return True
	def dfs(board, x, y):
		if x > 8 or y > 8:
			return True
		if board[x][y] == '.':
			for k in '123456789':
				if is_valid(board, x, y, k): #当前数字符合要求
					board[x][y] = k
					nextx = x
					nexty = y + 1
					if nexty == 9:
						nexty = 0
						nextx = nextx + 1
					if dfs(board, nextx, nexty): #搜索下一个空格
						return True
					board[x][y] = '.'
			return False  #无满足条件存在， 数独无解
		else: #当前非空格， 即有数字， 跳过继续深搜
			nextx = x
			nexty = y+1
			if nexty == 9:
				nexty = 0
				nextx = nextx + 1
			return dfs(board, nextx, nexty)


