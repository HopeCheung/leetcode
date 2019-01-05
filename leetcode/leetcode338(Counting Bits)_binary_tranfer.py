class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = []
        for i in range(num+1):
            res.append(sum([1 for bit in bin(i)[2:] if bit == "1"]))
        return res

class Solution2:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = [0]
        for i in range(1, num+1):
            res.append(res[i//2] + i % 2)
        return res