class Solution:
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        def judge(i, j, num):
            first, second, k = num[:i], num[i:j], j
            while k < len(num):
                curr = str(int(first) + int(second))
                if curr != num[k:][:len(curr)] or (first != "0" and first[0] == "0") or (second != "0" and second[0] == "0"):
                    return False
                else:
                    k = k + len(curr)
                    first, second = second, curr
            return True
            
        if len(num) < 3:
            return False
        
        for i in range(1, len(num)-1):
            for j in range(i+1, len(num)):
                if judge(i, j, num):
                    return True
        return False