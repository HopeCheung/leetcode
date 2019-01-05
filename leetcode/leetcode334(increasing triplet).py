class Solution:
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first = second = float("inf")
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False

class Solution2:
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        prev = []
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                if len(prev) == 0:
                    prev = [nums[i-1], nums[i]]
                else:
                    if nums[i] > prev[1] or nums[i-1] > prev[0]:
                        return True
                    else:
                        prev[0], prev[1] = nums[i-1], nums[i]
        return False