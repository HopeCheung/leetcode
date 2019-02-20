class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if nums == []:
            return [] 
        
        nums = sorted(nums)
        dp = [[nums[i]] for i in range(len(nums))]
        
        for i in range(1, len(nums)):
            for j in reversed(range(0, i)):
                if nums[i] % nums[j] == 0 and len(dp[j]) >= len(dp[i]):
                    dp[i] = dp[j] + [nums[i]]
                    
        return max(dp, key=len) if len(dp) != 0 else []

    
    

            
                    
        