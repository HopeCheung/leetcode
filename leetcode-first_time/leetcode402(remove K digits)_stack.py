class Solution:
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if k >= len(num):
            return "0"
        
        stack = []
        for i in range(len(num)):
            while stack and k > 0 and num[i] < stack[-1]:
                stack.pop()
                k = k - 1
            stack.append(num[i])
            
        if len(stack) == 0:
            return "0"
        stack = stack[:-k] if k != 0 else stack
        return str(int("".join(stack)))
        
        
        
        