class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 0:
            return []
        i, column_zero, row_zero = 0, [], []
        while i < len(matrix):
            j = 0
            while j < len(matrix[0]):
                if j in column_zero or matrix[i][j] != 0:
                    j = j + 1
                elif matrix[i][j] == 0:
                    for l in range(len(matrix)):
                        if matrix[l][j] == 0:
                            row_zero.append(l)
                        matrix[l][j] = 0
                    column_zero.append(j)
                    row_zero.append(i)
                    j = j + 1
            i = i + 1
        for k in row_zero:
            for r in range(len(matrix[0])):
                matrix[k][r] = 0

###################---------------------------------
class Solution2:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 0:
            return []
        zero_record = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zero_record.append((i, j))
        for elem in zero_record:
            for i in range(len(matrix)):
                matrix[i][elem[1]] = 0
            for j in range(len(matrix[0])):
                matrix[elem[0]][j] = 0

##################----------------------------------O(m+n)