class Solution(object):
    
    def dfs(self, num, hours, minutes, hour_try, min_try, result):
        if hour_try >= 12 or min_try >= 60:
            return
        if num == 0:
            minutes = hour_try * 60 + min_try
            result.append("%d:%02d" %(minutes // 60, minutes % 60))
            return
        if hours:
            self.dfs(num, hours[1:], minutes, hour_try, min_try, result)
            self.dfs(num - 1, hours[1:], minutes, hour_try + hours[0], min_try, result)
        elif minutes:
            self.dfs(num, hours, minutes[1:], hour_try, min_try, result)
            self.dfs(num - 1, hours, minutes[1:], hour_try, min_try + minutes[0], result)
        return 
            
        
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        
        hours, minutes, result = [1, 2, 4, 8], [1, 2, 4, 8, 16 ,32], []
        self.dfs(num, hours, minutes, 0, 0, result)
        return result