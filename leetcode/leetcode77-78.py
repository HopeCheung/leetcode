class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if n == 0 or k == 0:
            return []
        result = []
        
        def helper(start, n, k, curr):
            if k == 0:
                result.append(curr[:])
                return 
            elif start > n-k+1:
                return
            for i in range(start, n-k+2):
                curr = curr + [i]
                helper(i+1, n, k-1, curr)
                curr.pop()
        
        helper(1, n, k, [])
        return result
                