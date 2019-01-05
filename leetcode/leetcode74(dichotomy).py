class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        def keep_search(line, target):
            left, right = 0, len(line) - 1
            while left <= right:
                mid = (left + right) // 2
                if line[mid] == target:
                    return True
                elif line[mid] > target:
                    right = mid - 1
                elif line[mid] < target:
                    left = mid + 1
            return False
            
        if len(matrix) == 0:
            return False
        
        top, down, target_line = 0, len(matrix) - 1, []
        while top <= down:
            mid = (top + down) // 2
            if top == down:
                target_line = matrix[mid]
                break
            elif mid == len(matrix) - 1:
                target_line = matrix[len(matrix) - 1]
                break
            else:
                if target in range(matrix[mid][0], matrix[mid+1][0]):
                    target_line = matrix[mid]
                    break
                elif target < matrix[mid][0]:
                    down = mid - 1 
                elif target > matrix[mid+1][0]:
                    top = mid + 1
                elif target == matrix[mid][0] or target == matrix[mid+1][0]:
                    return True
        if target_line == []:
            return False
        return keep_search(target_line, target)