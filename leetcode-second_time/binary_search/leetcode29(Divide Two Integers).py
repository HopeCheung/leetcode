class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0:
            return - 1
        if dividend == 0:
            return 0
        
        symbol = -1 if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0) else 1
        dividend, divisor = abs(dividend), abs(divisor)
        if dividend < divisor:
            return 0
        orgin = divisor
        
        while divisor < dividend:
            divisor = divisor * 2
        divisor = divisor if divisor == dividend else divisor // 2
        
        ans = 0
        while dividend >= 0 and divisor >= orgin:
            if dividend >= divisor:
                ans, dividend = ans * 2 + 1, dividend - divisor
            else:
                ans = ans * 2
            divisor = divisor // 2
        ans = ans if symbol == 1 else -ans
        
        if ans > pow(2, 31) - 1 or ans < -pow(2, 31):
            return pow(2, 31) - 1
        else:
            return ans
            
                
            
            
            