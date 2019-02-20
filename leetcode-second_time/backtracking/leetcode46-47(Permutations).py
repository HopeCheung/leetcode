class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def helper(nums, visited):
            if nums in visited:
                return visited
            else:
                visited.append(nums)
                return helper(next_num(nums[:]), visited) 
        
        def next_num(nums):
            i = len(nums) - 2
            while i >= 0:
                for j in range(i+1, len(nums)):
                    if nums[j] > nums[i]:
                        nums[i], nums[j] = nums[j], nums[i]
                        nums[i+1:] = sorted(nums[i+1:])
                        return nums
                nums[i:] = sorted(nums[i:])
                i = i - 1
            return nums
        return helper(nums, [])
        


