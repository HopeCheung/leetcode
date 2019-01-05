class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) < 2:
            return []
        output = []
        
        prefix = 1
        for i in range(len(nums)):
            output.append(prefix)
            prefix = prefix * nums[i]
            
        postfix = 1
        for j in range(len(nums)-1, -1, -1):
            output[j] = output[j] * postfix
            postfix = postfix * nums[j]
        
        return output
            
        