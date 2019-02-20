class Solution1:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []
        res = []
        def helper(stack, path, n):
            if n == 0 and stack == []:
                res.append(path[:])
            elif n == 0:
                curr = stack.pop()
                helper(stack, path + curr, n)
                stack.append(curr)
            else:
                if stack == []:
                    stack.append(")")
                    helper(stack, path + "(", n - 1)
                    stack.pop()
                else:
                    stack.append(")")
                    helper(stack, path + "(", n - 1)
                    stack.pop()
                    curr = stack.pop()
                    helper(stack, path + curr, n)
                    stack.append(curr)
        helper([], "", n)
        return res
            
class Solution2:
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
            
            
            
        