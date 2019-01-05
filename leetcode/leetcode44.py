class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        i = 0
        while i < len(p) - 1:
            if p[i] == '*' and p[i+1] == '*' :
                p = p[:i] + p[i+1:]
            else:
                i = i + 1
        if p == s:
            return True
        if len(s) == 0 and p == '*':
            return True
        if (len(p) == 0) or (len(s) == 0 and p != '*'):
            return False

        
        while len(s) != 0 and len(p) != 0:
            if p[0] == s[0] or p[0] == '?':
                s, p = s[1:], p[1:]
            elif p[0] == '*':
                if len(p) == 1:
                    return True
                while len(s) != 0 and p[1] != s[0] and p[1] != '?':
                    s = s[1:]
                if len(s) == 0 and len(p) == 0:
                    return True
                if len(s) == 0 and len(p) != 0:
                    return False
                if self.isMatch(s[1:], p[2:]):
                    return True
                else:
                    s = s[1:]
            else:
                return False
        if len(s) == 0 and (len(p) == 0 or p == '*' ):
            return True
        return False

###################### --------------------------------time limit
class Solution2:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        i, j, match, starIdx = 0, 0, 0, -1
        while i < len(s):
            if j < len(p) and (p[j] == '?' or s[i] == p[j]):
                i = i + 1
                j = j + 1
            elif j < len(p) and p[j] == '*':
                starIdx = j
                match = i
                j = j + 1
            elif starIdx != -1:
                j = starIdx + 1
                match = match + 1
                i = match
            else:
                return False
        while j < len(p) and p[j] == '*':
            j = j + 1
        return j == len(p)
    
                        
                    
                    
            

            
    
                        
                    
                    
            
        