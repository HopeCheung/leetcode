from heapq import *
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if len(nums1) * len(nums2) == 0:
            return []
        
        visited, heap, res = [], [], []
        
        heappush(heap, (nums1[0]+nums2[0], 0, 0))
        visited.append((0, 0))
        
        while len(res) < k and heap:
            val = heappop(heap)
            res.append([nums1[val[1]], nums2[val[2]]])
            
            if val[1] + 1 < len(nums1) and (val[1]+1, val[2]) not in visited:
                heappush(heap, (nums1[val[1]+1]+nums2[val[2]], val[1]+1, val[2]))
                visited.append((val[1]+1, val[2]))
            
            if val[2] + 1 < len(nums2) and (val[1], val[2]+1) not in visited:
                heappush(heap, (nums1[val[1]]+nums2[val[2]+1], val[1], val[2]+1))
                visited.append((val[1], val[2]+1))
                
        return res
 
# https://docs.python.org/3/library/heapq.html       
    
    