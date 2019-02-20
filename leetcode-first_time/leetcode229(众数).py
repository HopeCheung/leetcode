class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []
        elif len(nums) == 1:
            return nums
        result = []
        
        m1, m2, c1, c2 = nums[0], 0, 1, 0
        for i in range(1, len(nums)):
            x = nums[i]
            if x == m1:
                c1 = c1 + 1
            elif x == m2:
                c2 = c2 + 1
            elif c1 == 0:
                m1 = x
                c1 = 1
            elif c2 == 0:
                m2 = x
                c2 = 1
            else:
                c1 = c1 - 1
                c2 = c2 - 1
                
        c1, c2 = 0, 0
        for i in range(len(nums)):
            if m1 == nums[i]:
                c1 = c1 + 1
            elif m2 == nums[i]:
                c2 = c2 + 1
        
        if c1 > len(nums) // 3:
            result.append(m1)
        if c2 > len(nums) // 3:
            result.append(m2)
        return result
####--------Boyer-Moore Voting Algorithm
        
