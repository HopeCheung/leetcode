class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        nums.sort()
        
        i, count, result = 0, 1, []
        while i < len(nums) - 1:
            if nums[i+1] == nums[i] + 1:
                count, i = count + 1, i + 1
            elif nums[i+1] == nums[i]:
                i = i + 1
            else:
                result.append(count)
                count, i = 1, i + 1
        result.append(count)
        return max(result)
                
###-----sort function used
class Solution(object):
    def longestConsecutive(self, nums):

        n = len(nums)
        d = {}
        ans = 0
        for i in nums:
            if i not in d:
                left = d.get(i-1, 0) #get返回dic指定键的值，如果键不在字典中，返回一个指定值，默认为None
                right = d.get(i+1, 0)
                length = left + right + 1
                ans = max(ans, length)

                d[i] = length
                d[i-left] = length
                d[i+right] = length

        return ans
###------hash table
