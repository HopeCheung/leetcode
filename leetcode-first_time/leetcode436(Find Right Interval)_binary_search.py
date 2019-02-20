# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        def search(target, nums):
            ans = float("inf")
            left, right = 0, len(nums)-1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return new_nums.index(nums[mid])
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    ans = min(ans, nums[mid])
                    right = mid - 1
            return new_nums.index(ans) if ans != float("inf") else -1

        if len(intervals) <= 1:
            return [-1]
        
        backup = [0] * len(intervals)
        new_nums = [elem.start for elem in intervals]
        right_num = sorted(new_nums)
        for i in range(len(intervals)):
            backup[i] = search(intervals[i].end, right_num)
            
        return backup