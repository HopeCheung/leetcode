class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        
        hold, not_hold, cool_down = float("-inf"), 0, float("-inf")
        for p in prices:
            hold, not_hold, cool_down = max(hold, not_hold - p), max(cool_down, not_hold), hold+p
        
        return max(not_hold, cool_down)
        
                
        
                