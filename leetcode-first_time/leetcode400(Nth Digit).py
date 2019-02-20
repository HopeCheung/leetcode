class Solution:
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 9:
            return n
        
        curr, index = 9, 1
        while n > 0:
            n = n - curr * index
            curr, index = curr * 10, index + 1
        curr, index = curr // 10, index - 1
        
        n = n + curr * index
        num, pos = n // index, n % index
        final_num = int(("9" * (index-1))) + num

        if pos == 0:
            return int(str(final_num)[-1])
        else:
            return int(str(final_num+1)[pos-1])
        


            
            
        