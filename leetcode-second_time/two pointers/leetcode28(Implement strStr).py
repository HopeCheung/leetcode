class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle not in haystack:
            return -1        
        if needle == "":
            return 0
        
        first = 0
        while first <= len(haystack) - len(needle):
            if haystack[first] == needle[0]:
                end, i = first + 1, 1
                while end < len(haystack) and i < len(needle) and haystack[end] == needle[i]:
                    end, i = end + 1, i + 1
                if end - first == len(needle):
                    return first
            first = first + 1
        return -1

class Solution2:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle not in haystack:
            return -1
        if len(needle) == 0 or len(needle) == len(haystack):
            return 0          
        for i in range(0, len(haystack) - len(needle) + 1):
            if haystack[i : i+len(needle)] == needle:
                return i
            
        

            
        
            
        