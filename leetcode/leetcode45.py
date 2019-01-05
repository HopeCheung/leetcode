class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        
        result = []
        def helper(nums, count, length):
            if len(nums) == 0:
                return
            for i in range(1, nums[0] + 1):
                if i > length:
                    return
                else:
                    count = count + 1
                    if length - i == 0:
                        result.append(count)
                        return
                    helper(nums[i:], count, length-i)
                    count = count - 1

        helper(nums, 0, len(nums)-1)
        return min(result)

##########------------backtrack: time limit                
                    

