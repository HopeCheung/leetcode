class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        left, right = "", ""
        l, r = 0, len(s) - 1
        while l < r:
            if left == "":
                if s[l] in "aeiouAEIOU":
                    left = s[l]
                else:
                    l = l + 1
            if right == "":
                if s[r] in "aeiouAEIOU":
                    right = s[r]
                else:
                    r = r - 1
            if left != "" and right != "":
                s = s[:l] + s[r] + s[l+1:r] + s[l] + s[r+1:]
                left, right = "", ""
                l, r = l + 1, r - 1
        return s
###-------memory exceed---------------------------
class Solution2(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        left, right = "", ""
        l, r = 0, len(s) - 1
        s = list(s)
        while l < r:
            if left == "":
                if s[l] in "aeiouAEIOU":
                    left = s[l]
                else:
                    l = l + 1
            if right == "":
                if s[r] in "aeiouAEIOU":
                    right = s[r]
                else:
                    r = r - 1
            if left != "" and right != "":
                s[l], s[r] = s[r], s[l]
                left, right = "", ""
                l, r = l + 1, r - 1
        return "".join(s)
###chage str to list
        
