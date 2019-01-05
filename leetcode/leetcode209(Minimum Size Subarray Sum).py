class Solution1(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, 0
        res = float('inf')
        while left < len(nums):
            while right < len(nums) and s > sum(nums[left:right+1]):
                right = right + 1
            if sum(nums[left:right+1]) >= s:
                res = min(res, right - left + 1)
                left = left + 1
            else:
                break
        if res != float('inf'):
            return res
        return 0
#-----------slow
class Solution2:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        ans = float('inf')  # ans的初始值为无穷大
        left, right = 0, 0  # 左右指针的初始值
        sum = 0
        while left < len(nums):
            while right < len(nums) and sum < s:
                sum += nums[right]
                right += 1

            # 当右指针超出索引，或者sum大于等于s时
            if sum >= s:
                ans = min(ans, right-left)

            sum -= nums[left]
            left += 1

        return ans if ans < float('inf') else 0  
##------fast         

