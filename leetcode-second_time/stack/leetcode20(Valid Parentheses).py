class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        
        stack = []
        i, backup = 0, {"(":")", "[":"]", "{":"}"} 
        while i < len(s):
            if s[i] in "([{":
                stack.append(s[i])
                i = i + 1
            elif len(stack) != 0 and backup[stack.pop()] == s[i]:
                i = i + 1
            else:
                return False
        if len(stack) != 0:
            return False
        return True