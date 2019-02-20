class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0 or prices == sorted(prices)[::-1]:
                return 0
            
        def helper(prices, profit, buy):
            if len(prices) == 0:
                return profit
            elif len(prices) == 1:
                if prices[0] < buy:
                    return profit
                else:
                    return profit + prices[0] - buy
            elif prices[0] < buy:
                return helper(prices[1:], profit, prices[0])
            else:
                return max(helper(prices[2:], profit + prices[0] - buy, prices[1]), helper(prices[1:], profit, buy))
            
        return helper(prices[1:], 0, prices[0])
#####----------time exceeded
class Solution2(object):
    def maxProfit(self, prices):
        ans=0
        if len(prices)<=1:
            return 0
        for x in range(1,len(prices)):
            if prices[x]-prices[x-1]>=0:
                ans+=prices[x]-prices[x-1]
        return ans
####-----------贪心算法