class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = []
        for elem in nums:
            if elem in res: 
                continue
            elif len(res) < 3:
                res.append(elem)
                res = sorted(res)
            else:
                for j in range(3):
                    if elem > res[j]:
                        res[j] = elem
                        res = sorted(res)
                        break
        #return res
        return res[-3] if len(res) >= 3 else max(res) 
#-------------------------------------------------------------------------
class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first, second, third = -float("inf"), -float("inf"), -float("inf")
        for n in nums:
            if n > first:
                first, second, third = n, first, second
            elif n > second and n != first:
                second, third = n, second
            elif n > third and n != first and n != second:
                third = n
        return third if third > -float("inf") else first
    

        

