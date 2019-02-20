class Solution:
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == "":
            return True
        if t == "":
            return False
        
        dp = [[False for j in range(len(t)+1)] for i in range(len(s)+1)]
        dp[0][0] = True
        
        for j in range(1, len(t)+1):
            dp[0][j] = True
        for i in range(1, len(s)+1):
            dp[i][0] = False
    
        for i in range(1, len(s)+1):
            for j in range(1, len(t)+1):
                if dp[i][j-1] == True or (dp[i-1][j-1] == True and s[i-1] == t[j-1]):
                    dp[i][j] = True
        return dp[len(s)][len(t)]
#-----------------2D_DP--------_TLE------------------------------------------------
class Solution2:
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == "":
            return True
        if t == "":
            return False
        
        dp =[0] * len(t)
        dp[0] = 1 if s[0] == t[0] else 0
        
        for i in range(1, len(t)):
            if dp[i] == len(s):
                return True
            for j in reversed(range(i)):
                mid = dp[j] + 1 if s[dp[j]] == t[i] else dp[j]
                dp[i] = max(dp[i], mid)
                
        return dp[len(t)-1] == len(s)
#-----------DP------------still TLE--------------------------------------------------
class Solution:
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if not s:
            return True
        
        s = list(s)
        for i in range(len(t)):
            if s[0] == t[i]:
                s.pop(0)

            if not s:
                return True

        return False
#-------------e.....-----------------------------------------------------------------
class Solution:
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if not s:
            return True
        
        i , j , lt , ls = 0 , 0 , len(t) , len(s)
        while j < ls and i < lt:
            if s[j] == t[i]:
                j+=1
            i+=1
        return j == ls
#-----------two points---------------------------------------------------------------
