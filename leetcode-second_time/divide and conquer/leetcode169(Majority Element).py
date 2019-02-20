class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return None
        if len(nums) == 1:
            return nums[0]
        
        def find(begin, end, nums):
            if begin == end:
                return nums[begin]
            
            mid = (begin + end) // 2
            left, right = find(begin, mid, nums), find(mid+1, end, nums)
            if left == right:
                return left
            
            cntL, cntR = 0, 0
            for i in range(begin, end+1):
                if nums[i] == left:
                    cntL = cntL + 1
                elif nums[i] == right:
                    cntR = cntR + 1
            
            return left if cntL >= cntR else right
        
        return find(0, len(nums)-1, nums)
        
        
            
            
            