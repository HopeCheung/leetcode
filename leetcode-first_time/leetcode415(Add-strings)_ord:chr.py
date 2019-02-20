class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        a, b = 0, 0
        
        for n in num1:
            a = a * 10 + ord(n) - 48
        for n in num2:
            b = b * 10 + ord(n) - 48
        res, ans = a + b, ""
        
        while res != 0:
            ans, res = chr(res%10 + 48) + ans, res // 10 
        return ans if ans != "" else "0"
        