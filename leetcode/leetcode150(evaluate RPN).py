class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        ans = []
        for i in tokens:
            if i != '/' and i != '*' and i != '+' and i != '-':
                ans.append(int(i))
            else:
                tmp1 = ans.pop()
                tmp2 = ans.pop()
                if i == '/':
                    if tmp1*tmp2 < 0:
                        ans.append(-((-tmp2) // tmp1))
                    else:
                        ans.append(tmp2 // tmp1)
                if i == '*':
                    ans.append(tmp2*tmp1)
                if i == '+':
                    ans.append(tmp2 + tmp1)
                if i == '-':
                    ans.append(tmp2 - tmp1)
        return ans[0]
