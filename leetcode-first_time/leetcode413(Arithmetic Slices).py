class Solution:
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) < 3:
            return 0
        
        def helper(num):
            if num < 3:
                return 0
            return sum(range(1, num-1))
        
        start, end, res = 0, 1, 0
        while end < len(A):
            diff = A[end] - A[start]
            while end < len(A) and A[end] - A[end -1] == diff:
                end = end + 1
            res = res + helper(end - start)
            start = end - 1
        
        return res
            
        