class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        def helper(heights, k):
            one_result = []
            height = 0
            for i in range(len(heights) - k + 1):
                height = min(heights[i:i+k])
                result.append(height * k)
            return one_result
        
        if len(heights) == 0:
            return 0
        
        result = []
        for k in range(1, len(heights)+1):
            result.extend(helper(heights, k))
        
        return max(result)
            
#########---------------slow
class Solution2:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if len(heights) == 0:
            return 0
        
        stack, max_s = [heights[0]], 0
        i = 1
        while i < len(heights):
            if heights[i] >= stack[len(stack) - 1]:
                stack.append(heights[i])
            else:
                count = 0
                while len(stack) != 0 and heights[i] < stack[len(stack) - 1]:
                    height = stack.pop()
                    count = count + 1
                    max_s = max(max_s, count*height)
                stack.extend([heights[i] for j in range(count+1)])
            i = i + 1
            
        candidate = 0
        for i in range(len(stack)):
            candidate = max(candidate, stack[i] * (len(stack)-i))
            
        return max(candidate, max_s)
#####-------https://www.cnblogs.com/ganganloveu/p/4148303.html

    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        def find_max(nums):
            stack, result = [nums[0]], 0
            i = 1 
            while i < len(nums):
                if nums[i] >= stack[len(stack)-1]:
                    stack.append(nums[i])
                else:
                    count = 0
                    while len(stack) != 0 and stack[len(stack)-1] > nums[i]:
                        height = stack.pop()
                        count = count + 1
                        result = max(result, count * height)
                    stack.extend([nums[i] for j in range(count+1)])
                i = i + 1
            for k in range(len(stack)):
                result = max(result, stack[k] * (len(stack) - k))
            return result
        
        if len(matrix) == 0:
            return 0
        
        result = []
        for j in range(len(matrix[0])):
            start = 0
            while start < len(matrix):
                i, length = start, 0
                while i < len(matrix):
                    if matrix[i][j] == '1':
                        length, i = length + 1, i + 1
                    else:
                        break
                matrix[start][j] = length
                start = start + 1
        
        for row in matrix:
            result.append(find_max(row))
        return max(result)
        

            
            

