class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def lower_band(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left
        
        def higher_band(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return right
        
        if target not in nums or len(nums) == 0 or (len(nums) == 1 and nums[0] != target):
            return [-1, -1]
        left = lower_band(nums, target)
        right = higher_band(nums, target)
        return [left, right]
                

            
                
            
        