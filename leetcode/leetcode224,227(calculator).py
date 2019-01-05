class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []  # res = sum(stack)
        num = 0
        sign = '+'  # default
        s += '+'  # add a char to force it processing the last number
        for char in s:
            if ord('0') <= ord(char) <= ord('9'):  # digit
                num = num * 10 + ord(char) - ord('0')
            else:  # finish scanning a number
                if char != ' ':
                    if sign == '+':  # last sign
                        stack.append(num)
                    elif sign == '-':
                        stack.append(-num)
                    elif sign == '*':
                        last = stack.pop()
                        stack.append(last*num)
                    elif sign == '/':
                        # 3//2 = 1, -3//2 = -2
                        # 14-3//2 != 14+(-3//2)
                        last = stack.pop()
                        if last < 0:
                            res = -(-last//num)
                        else:
                            res = last//num
                        stack.append(res)

                    # reset
                    sign = char
                    num = 0

        return sum(stack)

    def calculate2(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        
        def deal(s):
            if len(s) == 0:
                return ''
            i, a, b, backup = 0, '', '', []
            while i < len(s):
                if len(backup) == 0:
                    if s[i] == '+' or s[i] == '-':
                        backup.append(s[i])
                        i = i + 1
                    else:
                        a, i = a + s[i], i + 1
                else:   
                    if s[i] == '+' or s[i] == '-':
                        symbol = backup.pop()
                        backup.append(s[i])
                        if symbol == '+':
                            a, b = str((int(a) + int(b))), ''
                        elif symbol == '-':
                            a, b = str((int(a) - int(b))), ''
                        i = i + 1
                    else:
                        b, i = b + s[i] , i + 1
            if backup == []:
                return a
            symbol = backup.pop()
            if symbol == '+':
                a, b = str((int(a) + int(b))), ''
            elif symbol == '-':
                a, b = str((int(a) - int(b))), ''
            return a
        
        stack, i = [], 0
        while i < len(s):
            if s[i] == ' ':
                i = i + 1
            elif s[i] != ')':
                stack.append(s[i])
                i = i + 1
            else:
                store, j = '', len(stack) - 1
                while j >= 0 and stack[j] != '(':
                    j = j - 1
                stack = stack[:j] + [deal(stack[j+1:len(stack)])]
                i = i + 1
            
        return int(deal(stack))
                    

