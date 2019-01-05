# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 0:
            return []
        
        result = []
        for elem in intervals:
            if elem not in result:
                i, change = len(result) - 1, 0
                while i >= 0:
                    if range(result[i][0], result[i][1]+1) in range(elem[0], elem[1]+1):
                        result[i], change = elem, 1
                        break
                    elif range(elem[0], elem[1]+1) in range(result[i][0], result[i][1]+1):
                        change = 1
                        break
                    elif elem[0] in range(result[i][0], result[i][1]+1) and elem[1] > result[i][1]:
                        result[i][1], change = elem[1], 1
                        break
                    elif elem[1] in range(result[i][0], result[i][1]+1) and elem[0] < result[i][0]:
                        result[i][0], change = elem[0], 1
                        break
                    else:
                        i = i - 1
                if change == 0:
                    result = result + [elem[:]]
            else:
                continue
        return result
                        