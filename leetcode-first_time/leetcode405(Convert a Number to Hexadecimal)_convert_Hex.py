class Solution:
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"
        
        dic = {}
        for i in range(10):
            dic[i] = str(i)
        for j in range(10, 16):
            dic[j] = "abcdef"[j-10]
            
        res = ""
        while len(res) < 8:
            num, res = num // 16, dic[num%16] + res
        
        while res and res[0] == "0":
            res = res[1:]
        if res == "":
            return "0"
        
        return res
            
            