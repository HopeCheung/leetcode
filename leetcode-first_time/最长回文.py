class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def complement(s):
            imin = 0
            imax = len(s) - 1
            while imin < imax:
                if s[imin] != s[imax]:
                    return False
                else:
                    imin = imin + 1
                    imax = imax - 1
            return True
        
        s_invert = s[::-1]
        store = []
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s_invert[i:j+1] in s and complement(s_invert[i:j+1]):
                    store.append(s_invert[i:j+1])
        if store: 
            max_len = max([len(elem) for elem in store])
            return [elem for elem in store if len(elem) == max_len][0]
        else:
            return ""

class Solution2(object):
    def longestPalindrome(self, s):
        res = ""
        for i in range(len(s)):            
            tmp = self.helper(s,i,i)
            #odd case like aba
            if(len(tmp)>len(res)):
                res = tmp
                
            tmp = self.helper(s,i,i+1)
            #even case like abba
            if(len(tmp)>len(res)):
                res = tmp
        return res
            
    # get the longest palindrome, l, r are the middle indexes   
    # from inner to outer            
    def helper(self,s,l,r):
        while l>=0 and r<len(s) and s[l]==s[r]:
            l -=1
            r +=1
        return s[l+1:r]
