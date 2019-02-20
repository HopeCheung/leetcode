class Solution:
    def longestValidParentheses(self, s):
        dp = [0] * len(s)
        for i in range(len(s)):
            if s[i] == "(":
                dp[i] = 0
            else:
                if i - 1 >= 0:
                    if s[i-1] == "(":
                        dp[i] = dp[i-2] + 2 if i-2 >= 0 else 2
                    else:
                        if i-1-dp[i-1] >= 0 and s[i-1-dp[i-1]] == "(":
                            dp[i] = dp[i-1] + 2
                            if i - 2 - dp[i-1] >= 0:
                                dp[i] = dp[i] + dp[i-2-dp[i-1]]
        return max(dp) if dp != [] else 0
                    

                
            
        