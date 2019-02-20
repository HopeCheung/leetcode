class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length = 0
        if s is None or len(s) == 0:
            return max_length
        d = {}
        one_max = 0
        indice = 0
        for i in range(len(s)):
            if s[i] in d and d[s[i]] >= indice:
                indice = d[s[i]] + 1
            d[s[i]] = i
            one_max = i + 1 - indice
            max_length = max(max_length, one_max)
        return max_length
    