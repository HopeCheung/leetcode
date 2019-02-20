# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if intervals == []:
            return 0
        ans = 0
        intervals = sorted(intervals, key = lambda x : x.end)
        i, curr, ans = 1, intervals[0].end, ans + 1
        while i < len(intervals):
            j = i + 1
            while i < len(intervals) and intervals[i].start < curr:
                i = i + 1
            if i == len(intervals):
                break
            else:
                curr, ans = intervals[i].end, ans + 1
        return len(intervals) - ans
            

        
        
        
        