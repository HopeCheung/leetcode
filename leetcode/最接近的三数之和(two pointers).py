class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        closest = 0
        diff = 999
        for i in range(len(nums)-2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                temp_sum = nums[i] + nums[left] + nums[right]
                temp_diff = abs(temp_sum - target)
                if temp_diff < diff:
                    diff = temp_diff
                    closest = temp_sum
                if temp_sum < target:
                    left = left + 1
                elif temp_sum > target:
                    right = right - 1
                else:
                    return temp_sum
        return closest