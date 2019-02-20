class Solution:
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) == 0:
            return 0
        
        s, k, ans = sum(A), len(A), sum([i * A[i] for i in range(len(A))])
        F = ans
        while A:
            F = F + s - k * A.pop()
            ans = max(ans, F)
        return ans
        
            
        