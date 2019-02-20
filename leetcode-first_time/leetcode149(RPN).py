class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if len(tokens) == 0:
            return 0
        
        def to_num(s):
            symbol = 1
            if s[0] == '+':
                symbol, s = 1, s[1:]
            if s[0] == '-':
                symbol, s = -1, s[1:]
            i, result = 0, 0
            while i < len(s):
                result = result * 10 + ord(s[i]) - 48
                i = i + 1
            return symbol * result
        
        def transfer(tokens):
            i = 0
            while i < len(tokens):
                if tokens[i] not in ['+', '-', '*', '/']:
                    tokens[i] = to_num(tokens[i])
                i = i + 1
            return tokens
                        
        
        stack, tokens = [], transfer(tokens)
        i = 0
        while i < len(tokens):
            if tokens[i] not in ['+', '-', '*', '/']:
                stack.append(tokens[i])
            else:
                op1 = stack.pop()
                op2 = stack.pop()
                if tokens[i] == '+':
                    stack.append(op2 + op1)
                elif tokens[i] == '-':
                    stack.append(op2 - op1)
                elif tokens[i] == '*':
                    stack.append(op2 * op1)
                elif tokens[i] == '/':
                    stack.append((op2 // abs(op1)) * (op1 // abs(op1)))
                print(stack[len(stack) - 1])
            i = i + 1
        return stack[0]

