class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        if z > x + y:
            return False
        if x == 0 and y == 0:
            return True
        
        if y < x:
            x, y = y, x
 
        while x != 0:
            r = y % x
            y, x = x, r
        
        return z % y == 0
            