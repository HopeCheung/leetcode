class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def do_add(n, result, right, left, path):
            if left == n and right == n:
                result.append(path)
                return
            if left < n:
                do_add(n, result, right, left + 1, path + '(')
                if right < left:
                    do_add(n, result, right + 1, left, path + ')')
            elif right < n:
                do_add(n, result, right + 1, left, path + ')')
                
        result = []
        do_add(n, result, 0, 0, '')
        return result
            
            
            
            
        