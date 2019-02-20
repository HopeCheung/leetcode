
class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) == 0 or val not in nums:
            return len(nums)
        
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums[i:] = nums[i+1:]
            else:
                i = i + 1
        return len(nums)

#optimize
class Solution2:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i = i + 1
        return i
        
            
        