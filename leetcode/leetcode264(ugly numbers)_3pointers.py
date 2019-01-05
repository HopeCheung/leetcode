class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0 or n > 1690:
            return False
        if n == 1:
            return 1
        
        ugly = [1]
        i2, i3, i5 = 0, 0, 0
        while n > 1:
            u2, u3, u5 = 2 * ugly[i2], 3 * ugly[i3], 5 * ugly[i5]
            u = min(u2, u3, u5)
            if u == u2:
                i2 = i2 + 1
            if u == u3:
                i3 = i3 + 1
            if u == u5:
                i5 = i5 + 1
            ugly.append(u)
            n = n - 1
        return ugly[-1]
        
        
    

