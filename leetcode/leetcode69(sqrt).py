class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        n = 0
        while n * n <= x:
            n = n + 1
        return n - 1
#####----------time limit

class Solution2:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 1 or x == 0:
            return x
        begin, end, result, mid = 0, x, 0, 0
        while abs(result - x) > 0.01:
            mid = (begin + end) / 2
            result = mid * mid
            if result > x:
                end = mid
            elif result < x:
                begin = mid
        if x in range(int(mid)* int(mid), (int(mid) + 1) * (int(mid) + 1)):
            return int(mid)
        return int(mid) + 1
###########----------dichotomy(faster)

class Solution3:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        pre, cur = 0.01, x
        while abs(cur - pre) > 0.01:
            pre = cur
            cur = (pre/2 + x/(2*pre))
        if x in range(int(cur)* int(cur), (int(cur) + 1) * (int(cur) + 1)):
            return int(cur)
        return int(cur) + 1
#########-----Newton's method(fastest)
#https://baike.baidu.com/item/牛顿迭代法/10887580?fr=aladdin

            

        
            
