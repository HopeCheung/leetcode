class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        def binary_search(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return True
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return False
        
        if len(nums) == 0:
            return False
        pivot = len(nums) - 1
        
        for i in range(len(nums)-1):
            if nums[i+1] < nums[i]:
                pivot = i
        
        if target > nums[pivot]:
            return False
        if pivot == len(nums) - 1:
            return binary_search(nums, target)
        else:
            return binary_search(nums[pivot+1:], target) or binary_search(nums[:pivot+1], target)
        
        
            