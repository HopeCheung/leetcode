class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        dp1, dp2 = [1] * len(nums), [1] * len(nums)
        
        for i in range(1, len(nums)):
            for j in reversed(range(i)):
                if dp1[j] % 2 == 0 and nums[i] < nums[j]:
                    dp1[i] = max(dp1[i], dp1[j] + 1)
                if dp1[j] % 2 == 1 and nums[i] > nums[j]:
                    dp1[i] = max(dp1[i], dp1[j] + 1)
                    
                if dp2[j] % 2 == 0 and nums[i] > nums[j]:
                    dp2[i] = max(dp2[i], dp2[j] + 1)
                if dp2[j] % 2 == 1 and nums[i] < nums[j]:
                    dp2[i] = max(dp2[i], dp2[j] + 1)
                    
        return max(max(dp1), max(dp2))
                    
class Solution2(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        up, down = [1] * len(nums), [1] * len(nums)
        
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    up[i] = max(up[i], down[j] + 1)
                elif nums[i] < nums[j]:
                    down[i] = max(down[i], up[j] + 1)
                    
        return max(up[-1], down[-1])
#-------------DP-----------------------------------------------
class Solution3(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)
        
        prev = nums[1] - nums[0]
        count = 2 if prev != 0 else 1
        
        for i in range(2, len(nums)):
            diff = nums[i] - nums[i-1]
            if diff > 0 and prev <= 0 or diff < 0 and prev >= 0:
                count, prev = count + 1, diff
        
        return count
#------------greddy----------------------------------------------