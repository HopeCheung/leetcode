class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def partition(left, right, nums):
            pivot = nums[right]
            split = left - 1
            for j in range(left, right):
                if nums[j] <= pivot:
                    nums[j], nums[split + 1] = nums[split+1], nums[j]
                    split = split + 1
            nums[right], nums[split+1] = nums[split+1], nums[right]
            return split + 1
        
        pivot = nums[len(nums)-1]
        left, right = 0, len(nums) - 1
        while 1:
            pos = partition(left, right, nums)
            if pos == len(nums) - k:
                return nums[pos]
            elif pos < len(nums) - k:
                left = pos + 1
            else:
                right = pos - 1
            
            
                
        
        
        