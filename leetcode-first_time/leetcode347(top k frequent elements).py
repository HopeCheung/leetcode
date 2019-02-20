class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] = dic[i] + 1
            else:
                dic[i] = 1
        
        dic = sorted(dic.items(), key = lambda item: item[1])
        res = [elem[0] for elem in dic][::-1][:k]
        return res