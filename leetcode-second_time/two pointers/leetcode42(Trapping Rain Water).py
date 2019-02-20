class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height) - 1
        while l < r and height[l] <= height[l+1]:
            l = l + 1
        while l < r and height[r] <= height[r-1]:
            r = r - 1
            
        square = 0
        while l < r:
            left, right = height[l], height[r]
            if left <= right:
                while l < r and height[l+1] < left:
                    l = l + 1
                    square = square + left - height[l]
                l = l + 1
            else:
                while l < r and height[r-1] < right:
                    r = r - 1
                    square = square + right - height[r]
                r = r - 1
        return square
        