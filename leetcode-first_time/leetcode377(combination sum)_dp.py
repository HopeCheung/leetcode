class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums == [] or target == 0:
            return 0
        
        dp = [0] * (target + 1)
        dp[0] = 1
        
        for i in range(1, target+1):
            for j in range(len(nums)):
                if i >= nums[j]:
                    dp[i] = dp[i] + dp[i-nums[j]]
        return dp[target]