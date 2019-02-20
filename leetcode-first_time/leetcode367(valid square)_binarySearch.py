class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0 or num == 1:
            return True
        
        left, right = 0, num // 2
        while left <= right:
            mid = (left + right) // 2
            val = mid * mid
            if val == num:
                return True
            elif val > num:
                right = mid - 1
            else:
                left = mid + 1
        return False
        