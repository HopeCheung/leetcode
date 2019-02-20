class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        
        def binary_search(nums, target):
            if len(nums) == 0:
                return 0
            left, right = 0, len(nums)-1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return left
        
        res = []
        for n in nums:
            pos = binary_search(res ,n)
            if pos >= len(res):
                res.append(n)
            else:
                res[pos] = n
        return len(res)