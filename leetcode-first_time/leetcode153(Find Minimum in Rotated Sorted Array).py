class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        elif nums == sorted(nums):
            return nums[0]
        
        def helper(nums):
            if len(nums) == 1:
                return nums[0]
            if len(nums) == 2:
                if nums != sorted(nums):
                    return min(nums)
                
            mid = len(nums) // 2
            if nums[:mid+1] == sorted(nums[:mid+1]):
                return helper(nums[mid:])
            elif nums[mid:] == sorted(nums[mid:]):
                return helper(nums[:mid+1])
        
        return helper(nums)
            
##--- O(lonN)
