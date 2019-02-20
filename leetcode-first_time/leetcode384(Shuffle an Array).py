import random
class Solution:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.backup = nums[:]
        self.lst = nums[:]
        

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.backup
        

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        ans = []
        while len(self.lst) > 0:
            pos = random.randint(0, len(self.lst)-1)
            ans.append(self.lst.pop(pos))
        self.lst = self.backup[:]
        return ans
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()