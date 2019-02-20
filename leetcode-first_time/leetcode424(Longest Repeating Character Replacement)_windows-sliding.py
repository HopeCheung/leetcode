class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        def find_max(lst):
            ans = 0
            for elem in set(lst):
                ans = max(ans, lst.count(elem))
            return ans
        
        if len(s) == 0 or k > len(s):
            return len(s)
        
        interval = k + 1
        i, res = 0, 0
        while i + interval <= len(s):
            if interval - find_max(s[i:i + interval]) <= k:
                interval, res = interval + 1, max(res, interval)
            else:
                i = i + 1
        return res
#---------------time-consuming-----------------------------------
