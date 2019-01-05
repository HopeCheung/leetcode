class Solution:
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        elif n in range(1, 10):
            return 1
        
        ones, m = 0, 1
        while m <= n:
            a, b = n // m, n % m
            ones = ones + (a + 8) // 10 * m
            if a % 10 == 1:
                ones = ones + b + 1
            m = m * 10
        return ones
        
        
            
            
        