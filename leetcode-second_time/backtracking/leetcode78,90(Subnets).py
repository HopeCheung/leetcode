class Solution:
    def subsets(self, nums: 'List[int]') -> 'List[List[int]]':
        nums = sorted(nums)
        res = []
        def helper(begin, path):
            if path not in res:
                res.append(path[:])
            for i in range(begin, len(nums)):
                helper(i+1, path+[nums[i]])
        helper(0, [])
        return res
        