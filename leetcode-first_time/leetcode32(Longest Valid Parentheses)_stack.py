class Solution:
    def longestValidParentheses(self, s):
        stack, maxCount, start = [], 0, 0
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                if stack != []:
                    stack.pop()
                    if stack == []:
                        maxCount = max(maxCount, i-start+1)
                    else:
                        maxCount = max(maxCount, i-stack[-1])
                else:
                    start = i + 1
        return maxCount

                
#https://blog.csdn.net/zhangxiao93/article/details/49103569
