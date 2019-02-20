class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low, high = 1, len(nums) - 1
        while low <= high:
            mid, cnt = (low + high) // 2, 0
            
            for n in nums:
                if n <= mid:
                    cnt = cnt + 1
            
            if cnt <= mid:
                low = mid + 1
            else:
                high = mid - 1
        return low
#---------------------binary-search--------------------------------
class Solution2:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow, fast = nums[0], nums[nums[0]]
        while slow != fast:
            slow, fast = nums[slow], nums[nums[fast]]
            
        fast = 0
        while slow != fast:
            slow, fast = nums[slow], nums[fast]
        return slow         
#---------------------two-points------------------------------------           
            

#https://www.cnblogs.com/jimmycheng/p/7519870.html