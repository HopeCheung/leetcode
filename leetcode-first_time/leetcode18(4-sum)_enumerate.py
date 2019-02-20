class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) < 4:
            return []
        
        nums, res = sorted(nums), []
        for i in range(len(nums)-2):
            temp1 = target - nums[i]
            for j in range(i+1, len(nums)-1):
                temp2 = temp1 - nums[j]
                new_nums = nums[j+1:]
                start, end = 0, len(new_nums) - 1
                while start < end:
                    if temp2 - new_nums[start] - new_nums[end] == 0:
                        if [nums[i], nums[j], new_nums[start], new_nums[end]] not in res:
                            res.append([nums[i], nums[j], new_nums[start], new_nums[end]])
                        start, end = start+1, end-1
                    elif temp2 - new_nums[start] - new_nums[end] > 0:
                        start = start + 1
                    else:
                        end = end - 1
        return res
#----------------------------------------------------------------------------------------------------
class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) < 4:
            return []
        
        nums, res = sorted(nums), []
        for x1, item1 in enumerate(nums):
            temp1 = target - item1
            for x2, item2 in enumerate(nums[x1+1:], x1):
                temp2 = temp1 - item2
                new_nums = nums[x2+2:]
                start, end = 0, len(new_nums) - 1
                while start < end:
                    if temp2 - new_nums[start] - new_nums[end] == 0:
                        if [item1, item2, new_nums[start], new_nums[end]] not in res:
                            res.append([item1, item2, new_nums[start], new_nums[end]])
                        start, end = start+1, end-1
                    elif temp2 - new_nums[start] - new_nums[end] > 0:
                        start = start + 1
                    else:
                        end = end - 1
        return res
#enumerate-------------------------------------------------------------------------------------------
