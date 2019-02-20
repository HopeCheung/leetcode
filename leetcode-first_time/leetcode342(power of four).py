class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        
        divide = 4
        while num % 4 == 0 or num == 1:
            if num == 1:
                return True
            elif divide > num:
                divide = divide // 4
            else:
                if num % divide == 0:
                    num, divide = num // divide, divide * 4
                else:
                    return False
        return False
        

class Solution2(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        
        new_num = bin(num)[2:]
        zero, one = 0, 0
        for digit in new_num:
            if digit == "1":
                one = one + 1
            else:
                zero = zero + 1
        return new_num[0] == "1" and one == 1 and zero % 2 == 0