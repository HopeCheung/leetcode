class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "":
            return []
        backup = {"0":" ", "1":"", "2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        res = []
        def helper(digits, curr, path):
            if curr == len(digits):
                res.append(path[:])
            else:
                for n in backup[digits[curr]]:
                    helper(digits, curr+1, path+n)
        helper(digits, 0, "")
        return res
        
        