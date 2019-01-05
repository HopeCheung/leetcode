class Solution:
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        miss, i, ans = 1, 0, 0
        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                i, miss = i + 1, miss + nums[i]
            else:
                miss, ans = miss * 2, ans + 1
        return ans