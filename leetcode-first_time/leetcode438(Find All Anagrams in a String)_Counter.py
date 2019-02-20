from collections import Counter
class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s) < len(p):
            return []
        
        p_char, counter, res = Counter(p), len(p), []
        for i in range(len(s)):
            if p_char[s[i]] >= 1:
                counter = counter - 1
            p_char[s[i]] = p_char[s[i]] - 1
            
            if i >= len(p):
                if p_char[s[i-len(p)]] >= 0:
                    counter = counter + 1
                p_char[s[i-len(p)]] = p_char[s[i-len(p)]] + 1
            if counter == 0:
                res.append(i-len(p)+1)
        return res
                
#http://www.pythoner.com/205.html
            
        