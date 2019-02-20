class Solution:
    def simplifyPath(self, path: 'str') -> 'str':    
        ans = path.split("/")
        i, stack =  0, []
        while i < len(ans):
            if ans[i] == "" or ans[i] == ".":
                i = i + 1
            elif ans[i] == "..":
                if len(stack) != 0:
                    stack.pop()
                i = i + 1
            else:
                stack.append(ans[i])
                i = i + 1
        ans = "/".join(stack)
        return "/" + ans
        