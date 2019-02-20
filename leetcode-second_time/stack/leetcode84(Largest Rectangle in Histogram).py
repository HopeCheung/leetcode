class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if len(heights) == 0:
            return 0
        
        stack, result, i = [heights[0]], 0, 1
        while i < len(heights):
            if heights[i] >= stack[-1]:
                stack.append(heights[i])
            else:
                cnt = 1
                while stack and stack[-1] > heights[i]:
                    result = max(result, cnt * stack.pop())
                    cnt = cnt + 1
                stack.extend(cnt*[heights[i]])
            i = i + 1
        for i in range(len(stack)):
            result = max(result, (i+1) * stack[-i-1])
        return result
        
            
            

