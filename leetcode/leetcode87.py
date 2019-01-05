class Solution:
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        def helper(s1, s2):
            if len(s1) != len(s2):
                return False
            if s1 == s2:
                return True
            if sorted(s1) != sorted(s2):
                return False
            
            for i in range(1, len(s1)):
                if helper(s1[:i], s2[:i]) and helper(s1[i:], s2[i:]):
                    return True
                if helper(s1[i:], s2[:len(s1) - i]) and helper(s1[:i], s2[len(s1) - i:]):
                    return True
            return False
        
        return helper(s1, s2)
        