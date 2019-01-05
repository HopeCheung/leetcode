class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        #dict.get(key, default=None)
        dic1 = dict()
        for num in nums1:
            dic1[num] = dic1.get(num,0) + 1
        
        dic2 = dict()
        for num in nums2:
            dic2[num] = dic2.get(num,0) + 1
            
        elements = list(set(nums1) & set(nums2))
        res = []
        for elem in elements:
            res = res + [elem] * min(dic1[elem], dic2[elem])
        
        return res
            
        