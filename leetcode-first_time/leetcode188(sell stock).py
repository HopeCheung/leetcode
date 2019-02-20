class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if k == 0 or len(prices) < 2:
            return 0
        
        if k >= len(prices) // 2:
            result = 0
            for i in range(1, len(prices)):
                if prices[i] > prices[i-1]:
                    result = result + prices[i] - prices[i-1]
            return result
        
        buy = [[0 for j in range(k+1)] for i in range(len(prices) + 1)]
        buy[0] = [-999 for j in range(k+1)]
        sell = [[0 for j in range(k+1)] for i in range(len(prices) + 1)]
        
        for i in range(1, len(prices) + 1):
            for j in range(1, k + 1):
                buy[i][j] = max(buy[i-1][j], sell[i][j-1]-prices[i-1])
                sell[i][j] = max(sell[i-1][j], buy[i][j] + prices[i-1])
        return sell[len(prices)][k]

###--https://blog.csdn.net/jmspan/article/details/51295053
        
        
        
        
