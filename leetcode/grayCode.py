class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = []
        for i in range(0, pow(2, n)):
            result.append(i ^ (i // 2))
        return result
        