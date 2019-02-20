class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
                return 0
        if len(nums) == 1:
                return nums[0]
            
        def no_cycle(nums):
            if len(nums) == 0:
                return 0
            if len(nums) == 1:
                return nums[0]
            if len(nums) == 2:
                return max(nums)
            if len(nums) == 3:
                return max(nums[1], nums[0] + nums[2])   
            dp = [0 for i in range(len(nums))]
            dp[0], dp[1], dp[2] = nums[0], nums[1], max(nums[1], nums[0] + nums[2])
            for i in range(3, len(nums)):
                dp[i] = max(dp[i-1], dp[i-2] + nums[i], dp[i-3] + nums[i])
            return dp[len(dp) - 1]
        
        return max(no_cycle(nums[1:]), no_cycle(nums[:-1]))
##--------dp method(slow)