class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        def helper(s):
            if s == "":
                return ""
            elif s[0] in "0123456789":
                i, num = 0, ""
                while s[i] in "0123456789":
                    num, i = num + s[i], i + 1
                    
                stack, j, i = [s[i]], i, i+1
                while i < len(s) and stack != []:
                    if s[i] == "[":
                        stack.append("[")
                        i = i + 1
                    elif s[i] == "]":
                        stack.pop()
                        i = i + 1
                    else:
                        i = i + 1
                if s[i:] == "":
                    return int(num) * helper(s[j+1:i-1])
                else:
                    return int(num) * helper(s[j+1:i-1]) + helper(s[i:])
            elif s[0] not in "0123456789[]":
                i, sym = 0, ""
                while i < len(s) and s[i] not in "0123456789[]":
                    sym, i = sym + s[i], i + 1
                return sym + helper(s[i:])
        
        return helper(s)

        
                
            
        