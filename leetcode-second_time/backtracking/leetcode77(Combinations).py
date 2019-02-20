class Solution:
    def combine(self, n: 'int', k: 'int') -> 'List[List[int]]':
        res = []
        def helper(begin, path, k):
            if k == 0:
                if path not in res:
                    res.append(path[:])
                return
            else:
                for i in range(begin, n+1):
                    helper(i+1, path+[i], k-1)
        helper(1, [], k)
        return res
                    
        