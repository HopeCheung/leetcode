class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        
        def dfs(left, right, nums):
            if left == right:
                return nums[left]
            mid = (left + right) // 2
            
            left_res, right_res = dfs(left, mid, nums), dfs(mid+1, right, nums)
            left_sum, right_sum = float("-inf"), float("-inf")
            
            Sum = 0
            for i in range(mid+1, right+1):
                Sum += nums[i]
                right_sum = max(right_sum, Sum)
            
            Sum = 0
            for j in range(mid, left-1, -1):
                Sum += nums[j]
                left_sum = max(left_sum, Sum)
            
            return max(left_res, right_res, left_sum+right_sum)
    
        return dfs(0, len(nums)-1, nums) 
                
        