class Solution:
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        def require(nums, max_num):
            num, total = 1, 0
            for i in range(len(nums)):
                total = total + nums[i]
                if total > max_num:
                    total = nums[i]
                    num = num + 1
            return num
        
        def upper_bound(nums, m):
            low, high = max(nums), sum(nums)
            while low < high:
                mid = (low + high) // 2
                target = require(nums, mid)
                if target > m:
                    low = mid + 1
                else:
                    high = mid
            return low
        
        return upper_bound(nums, m)
        
        