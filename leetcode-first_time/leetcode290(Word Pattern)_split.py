class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        pattern, str = list(pattern), str.split(' ')
        if len(pattern) != len(str):
            return False
        
        dic1, dic2 = {}, {}
        for p, s in zip(pattern, str):
            if p not in dic1:
                dic1[p] = s
            if s not in dic2:
                dic2[s] = p
            if (p in dic1 and dic1[p] != s) or (s in dic2 and dic2[s] != p):
                return False
        
        
        return True
            