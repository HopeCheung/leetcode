class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height)-1
        square = 0
        while l < r:
            square = max(square, (r-l) * min(height[l], height[r]))
            if height[l] < height[r]:
                l = l + 1
            else:
                r = r - 1
        return square
        
            
                
                
        