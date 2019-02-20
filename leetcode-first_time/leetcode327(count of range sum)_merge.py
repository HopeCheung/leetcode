class Solution:
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        self.sums = [0] 
        for n in nums:
            self.sums.append(self.sums[-1] + n)
        self.lower, self.upper = lower, upper
        
        return self.mergeSort(0, len(self.sums))
    
    def mergeSort(self, l, r):
        
        m = l + (r-l)//2
        if m == l:
            return 0
        
        count = self.mergeSort(l, m) + self.mergeSort(m, r)
        
        i = j = m
        
        for k in range(l, m):
            while i < r and self.sums[i] - self.sums[k] < self.lower:
                i += 1
            while j < r and self.sums[j] - self.sums[k] <= self.upper:
                j += 1
            count += j - i
            
        self.sums[l:r] = sorted(self.sums[l:r])
        return count