class Solution:
    def getPermutation(self, n: 'int', k: 'int') -> 'str':
        ans, backup = "", [str(i+1) for i in range(n)]
        def accumulate(n):
            if n == 0:
                return 0
            ans = 1
            while n >= 1:
                ans, n = ans * n, n - 1
            return ans
        
        while k >= 0 and n >= 1:
            inter, n, cnt = accumulate(n-1), n - 1, 0
            while inter != 0 and k > inter:
                k, cnt = k - inter, cnt + 1
            
            ans = ans + backup[cnt]
            backup.remove(ans[-1])
        return ans


