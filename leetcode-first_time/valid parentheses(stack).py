class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 != 0:
            return False
        
        dic = {'(':')', '[':']', '{':'}'}
        stack = []
        
        for i in s:
            if i in dic:
                stack.append(i)       #左括号进栈
            else:
                if not stack or dic[stack.pop()] != i:
                    return False      #此时栈不应空， 且出栈的应为右括号且与上一个左括号对应
        if stack:
            return False              #遍历结束， 栈空
        return True
        
                
                
            
        
