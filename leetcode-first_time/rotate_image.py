class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 0:
            return
        
        length = len(matrix)
        visited = {}
        for i in range(length):
            for j in range(length):
                visited[(i,j)] = matrix[i][j]
                if (length-1-j, i) in visited:
                    matrix[i][j] = visited[(length-1-j, i)]
                else:
                    matrix[i][j] = matrix[length-1-j][i]
        
     
#############------------better solution              
class Solution2:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 0:
            return 
        
        #按照主对角线，将对称元素交换
        for i in range(len(matrix)):
            for j in range(i+1):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        #按照列，将对称列元素全部交换
        i, j = 0, len(matrix) - 1
        while i < j:
            for k in range(len(matrix)):
                matrix[k][i], matrix[k][j] = matrix[k][j], matrix[k][i]
            i, j = i + 1, j - 1
        
                    
        