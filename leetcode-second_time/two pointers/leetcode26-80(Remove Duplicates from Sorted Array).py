#leetcode26
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        
        first, second = 0, 1
        while second < len(nums):
            if nums[first] == nums[second]:
                nums[second:] = nums[second+1:]
            else:
                first, second = first+1, second+1
        return len(nums)     
#optimize
class Solution2:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        
        first, second = 0, 1
        while second < len(nums):
            if nums[first] != nums[second]:
                first = first + 1
                nums[first] = nums[second]
            second = second + 1
        return first + 1

#leetcode80 Remove Duplicates from Sorted Array II
class Solution3:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return len(nums)
        
        
        first, second = 0, 1
        while second < len(nums):
            if nums[first] == nums[second]:
                if second - first > 1:
                    nums[second:] = nums[second+1:]
                else:
                    second = second + 1
            else:
                first = first + 1
        return len(nums)
                
                
        
                
        
