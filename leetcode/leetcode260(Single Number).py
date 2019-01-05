class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        first = 0
        second = 0
        xor = 0
        for n in nums:
            xor = xor ^ n
            
        xor &= -xor
        for num in nums:
            if num & xor == 0:
                first ^= num
            else:
                second ^= num
        
        return [first, second]