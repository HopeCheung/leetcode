# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if len(intervals) == 0:
            return [newInterval]
        
        i = 0
        while i < len(intervals):  
            if i == len(intervals) - 1:
                if newInterval.start > intervals[i].end:
                    intervals = intervals + [newInterval]
                    break
                elif newInterval.end < intervals[i].start:
                    intervals = intervals[0:i] + [newInterval] + intervals[i:]
                    break
                elif newInterval.start >= intervals[i].start and newInterval.end <= intervals[i].end:
                    break
                elif newInterval.start <= intervals[i].start and newInterval.end >= intervals[i].end:
                    intervals[i] = newInterval
                    break
                elif newInterval.start in range(intervals[i].start, intervals[i].end+1):
                    intervals[i].end = newInterval.end
                    break
                elif newInterval.end in range(intervals[i].start, intervals[i].end+1):
                    intervals[i].start = newInterval.start
                    break
            elif newInterval.end < intervals[i].start:
                intervals = intervals[0:i] + [newInterval] + intervals[i:]
                break
            elif newInterval.start < intervals[i].start:
                intervals[i].start = newInterval.start
                if newInterval.end in range(intervals[i].start, intervals[i].end+1):
                    break
                else:
                    if newInterval.end < intervals[i+1].start:
                        intervals[i].end = newInterval.end
                    else:
                        intervals[i].end = intervals[i+1].end
                        intervals = intervals[0:i+1] + intervals[i+2:]
            elif newInterval.start in range(intervals[i].start, intervals[i].end+1):
                if newInterval.end in range(intervals[i].start, intervals[i].end+1):
                    break
                else:
                    if newInterval.end < intervals[i+1].start:
                        intervals[i].end = newInterval.end
                        break
                    else:
                        intervals[i].end = intervals[i+1].end
                        intervals = intervals[0:i+1] + intervals[i+2:]
            else:
                i = i + 1
        return intervals                
#######----------------------really slow

class Solution2:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        intervals.append(newInterval)
        l = len(intervals)
        res = []
        intervals = sorted(intervals, key = lambda intervals:intervals.start)
        low = intervals[0].start
        high = intervals[0].end
        for i in range(1, l):
            if intervals[i].start <= high:
                high = max(high, intervals[i].end)
            else:
                res.append([low, high])
                low = intervals[i].start
                high = intervals[i].end
        res.append([low, high])
        return res
    
    def merge(self, intervals):
        intervals.sort(key=lambda x: x.start)

        merged = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not merged or merged[-1].end < interval.start:
                merged.append(interval)
            else:
            # otherwise, there is overlap, so we merge the current and previous
            # intervals.
                merged[-1].end = max(merged[-1].end, interval.end)

        return merged
