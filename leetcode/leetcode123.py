class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0 or prices == sorted(prices)[::-1]:
            return 0
        
        def dfs(prices, buy, count, profit):
            if count == 0 or len(prices) == 0:
                return profit
            elif buy == None:
                return max(dfs(prices[1:], buy, count, profit), dfs(prices[1:], prices[0], count, profit))
            elif prices[0] < buy:
                return dfs(prices[1:], buy, count, profit)
            else:
                return max(dfs(prices[1:], buy, count, profit), dfs(prices[1:], None, count - 1, profit + prices[0] - buy))
        
        return dfs(prices, None, 2, 0)
######---------dfs -- time exceeded
class Solution2(object):               
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0 or prices == sorted(prices)[::-1]:
            return 0
        
        def one_profit(prices):
            if len(prices) == 0:
                return 0
            if prices == sorted(prices)[::-1]:
                return 0      
            buy, i, profit = prices[0], 1, 0
            while i < len(prices):
                if prices[i] < buy:
                    buy = prices[i]
                else:
                    profit = max(profit, prices[i] - buy)
                i = i + 1 
            return profit
        
        profit = 0
        for i in range(len(prices)):
            profit = max(profit, one_profit(prices[i:]) + one_profit(prices[:i]))
            
        return profit
######-------still time exceeded
class Solution3(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0 or prices == sorted(prices)[::-1]:
            return 0
        
        profit = 0
        forw, back = [0 for i in range(len(prices))], [0 for j in range(len(prices))]
        
        curMin = prices[0]
        for i in range(1, len(prices)):
            curMin = min(curMin, prices[i])
            forw[i] = max(forw[i-1], prices[i] - curMin)
        
        curMax = prices[len(prices)-1]
        for j in range(len(prices)-2, -1, -1):
            curMax = max(curMax, prices[j])
            back[j] = min(back[j+1], prices[j] - curMax)
            
            profit = max(profit, forw[j] - back[j])
        
        return profit
#####-------https://www.cnblogs.com/ganganloveu/p/4128114.html

    
