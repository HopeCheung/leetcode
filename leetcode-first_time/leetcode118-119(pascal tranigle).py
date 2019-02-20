class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = [[1 for j in range(i+1)] for i in range(numRows)]
        i = 1
        while i < numRows:
            j = 1
            while j < i:
                result[i][j] = result[i-1][j-1] + result[i-1][j]
                j = j + 1
            i = i + 1
        
        return result
        
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        currrow = [1]
        if rowIndex == 0:
            return currrow
        
        for i in range(1, rowIndex+1):
            prerow, currrow = currrow, [1]
            for j in range(len(prerow)-1):
                currrow.append(prerow[j] + prerow[j+1])
            currrow.append(1)
        
        return currrow