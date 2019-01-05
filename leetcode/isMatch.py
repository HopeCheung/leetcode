class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """ 
        precede = ''
        if s in p:
            return True
        else:
            while len(p) != 0:
                if s[0] == p[0] or p[0] == '.':
                    precede = p[0]
                    s = s[1:]
                    if len(s) == 0:
                        return True
                    else:
                        p = p[1:]
                elif p[0] == '*':
                    if s[0] == precede or precede == '.':
                        s = s[1:]
                        if len(s) == 0:
                            return True
                    else:
                        p = p[1:]
                else:
                    p = p[1:]
        return False
