class Solution:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if sum(nums) % 2 != 0:
            return False
        mid = sum(nums) // 2
        nums.sort(reverse=True)
        
        def helper(i, target):
            if target == 0:
                return True
            elif i == len(nums) or target < 0 or nums[i] > target:
                return False
            else:
                return helper(i+1, target-nums[i]) or helper(i+1, target)
        
        return helper(0, mid)
#------iteration--------------------------------------------------------
class Solution:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) // 2
        nums.sort(reverse=True)
        
        dp = [[False for _ in range(target + 1)] for _ in range(len(nums) + 1)]
        for i in range(len(nums) + 1):
            dp[i][0] = True
        for i in range(1, len(nums) + 1):
            for j in range(1, target + 1):
                if j >= nums[i-1]:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
                    
        return dp[len(nums)][target]
#------DP ----slow---------------------------------------------------------------