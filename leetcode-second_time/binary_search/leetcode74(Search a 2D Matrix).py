class Solution:
    def searchMatrix(self, matrix: 'List[List[int]]', target: 'int') -> 'bool':
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        
        l, r = 0, len(matrix) - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                l = mid + 1
            else:
                r = mid - 1
        i = l - 1
         
        l1, r1 = 0, len(matrix[0]) - 1
        while l1 <= r1:
            mid = (l1 + r1) // 2
            if matrix[i][mid] == target:
                return True
            elif matrix[i][mid] < target:
                l1 = mid + 1
            else:
                r1 = mid - 1
        return False
        
            
        