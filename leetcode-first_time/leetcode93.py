class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) == 0:
            return []
        result = []
        
        def dfs(s, length, curr, count):
            if length == 0 and count == 0:
                if curr not in result:
                    result.append(curr[:-1])
                return 
            if count == 0 or len(s) == 0:
                return 
            else:
                if len(s) == 1 or s[0] == '0':
                    dfs(s[1:], length - 1, curr + s[0] + '.', count - 1)
                elif len(s) == 2 or int(s[0:3]) not in range(0, 256):
                    dfs(s[1:], length - 1, curr + s[0] + '.', count - 1)
                    dfs(s[2:], length - 2, curr + s[:2] + '.', count - 1)
                else:
                    dfs(s[1:], length - 1, curr + s[0] + '.', count - 1)
                    dfs(s[2:], length - 2, curr + s[:2] + '.', count - 1)
                    dfs(s[3:], length - 3, curr + s[:3] + '.', count - 1)
                    
        dfs(s, len(s), '', 4)
        return result
                    
                         