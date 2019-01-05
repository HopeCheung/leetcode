class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num = nums[0]
        def judge(nums, max_num):
            if len(nums) == 0:
                return max_num
            
            if max_num <= 0:
                return max(max_num, judge(nums[1:], nums[0]))
            else:
                if nums[0] >= 0:
                    return judge(nums[1:], max_num + nums[0])
                else:
                    if len(nums) == 1:
                        return max_num
                    else:
                        return max(max_num, judge(nums[1:], max_num + nums[0]))
       
        return judge(nums[1:], max_num)

###########------------memory limit exceeded
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num, ans = -pow(2, 31), 0
        for i in range(len(nums)):
            if ans < 0:
                ans = 0
            ans += nums[i]
            max_num = max(max_num, ans)
        return max_num
        
            