class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0 or len(s) == 1:
            return len(s)
        
        backup, res, symbol = set(s), 0, 0
        for t in set(s):
            if s.count(t) % 2 == 0:
                res = res + s.count(t)
            else:
                res = res + s.count(t) - 1
                symbol = 1
        
        return res + symbol
            
        
        
        