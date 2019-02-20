class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters = "abcdefghijklmnopqrstuvwxyz"
        res = [s.index(l) for l in letters if s.count(l) == 1]
        return min(res) if len(res) != 0 else -1