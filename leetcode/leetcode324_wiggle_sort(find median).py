class Solution:
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        mid = len(nums) // 2 if len(nums) % 2 == 0 else len(nums) // 2 + 1 
        nums[::2], nums[1::2] = nums[:mid][::-1], nums[mid:][::-1]