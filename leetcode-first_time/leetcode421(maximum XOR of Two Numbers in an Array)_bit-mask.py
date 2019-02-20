class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        
        mask, res = 0, 0
        for b in range(31, -1, -1):
            mask = mask | (1 << b) # set prefix b bits to be 1
            prefix = {mask & num for num in nums}  # mask the other bits of num
            
            guess = res | (1 << b) #gusee the current bit to be 1
            for p in prefix:
                if p ^ guess in prefix:
                    res = guess  # a ^ b = c => a ^ c = b
                    break
                    
        return res
        