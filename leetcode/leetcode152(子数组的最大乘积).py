class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        result = -999
        max_num, min_num = 1, 1
        for num in nums:
            t1, t2 = max_num * num, min_num * num
            max_num = max(num, max(t1, t2))
            min_num = min(num, min(t1, t2))
            result = max(max_num, result)
        return result
#####-----乘法中‘-’会对全局产生影响，因此要同时记录最大最小值