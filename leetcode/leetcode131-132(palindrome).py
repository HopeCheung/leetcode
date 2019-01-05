class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if len(s) == 0:
            return []
        
        def palindrome(s):
            if len(s) == 0:
                return False
            left, right = 0, len(s) - 1
            while left <= right:
                if s[left] == s[right]:
                    left, right = left + 1, right - 1
                else:
                    return False
            return True
        
        result = []
        def dfs(s, path):
            if s == '' and len(path) != 0:
                result.append(path[:])
            else:
                for i in range(len(s)):
                    if palindrome(s[:i+1]):
                        path.append(s[:i+1])
                        dfs(s[i+1:], path)
                        path.pop()
        dfs(s, [])
        return result

    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 2:
            return 0
        
        isPlain = [[False for j in range(len(s)+1)] for i in range(len(s)+1)] 
        for i in range(len(s)):
            isPlain[i][i] = True。#isPlain表示从i到j是否回文
        dp = [len(s)-i-1 for i in range(len(s) + 1)]  #dp表示从i到尾要切几次，初始化是假设只有单个字符回文
        
        for i in range(len(s), -1, -1):  #注意这里要从后往前， 因为dp[0]是最终结果，要从后往前推导
            for j in range(i, len(s)):
                if s[i] == s[j] and (isPlain[i+1][j-1] or j - i < 2):
                    dp[i] = min(dp[i], dp[j+1] + 1)  #如果i到j回文，那么dp[i]更新为dp[j+1]+1
                    isPlain[i][j] = True
        return dp[0]
        
        
