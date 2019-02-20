class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i, j = 0, 0 
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                i = i + 1
            else:
                nums1[i], nums2[j] = nums2[j], nums1[i]
                nums2.sort()
                
        nums1[m:] = nums2
        
        
            
        