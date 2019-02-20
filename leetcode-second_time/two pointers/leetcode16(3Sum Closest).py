class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums, ans, min_diff = sorted(nums), 0, float("inf")
        for i in range(len(nums)):
            left, right = i+1, len(nums) - 1
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                curr_diff = abs(curr_sum - target)
                if curr_diff < min_diff:
                    min_diff, ans = curr_diff, curr_sum
                if curr_sum == target:
                    return curr_sum
                elif curr_sum < target:
                    left = left + 1
                else:
                    right = right - 1
        return ans
        
                    
                    
        
        