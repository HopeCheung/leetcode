class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [0] + [-1] * amount
        for i in range(1, amount + 1):
            for j in range(len(coins)):
                if i >= coins[j] and dp[i-coins[j]] != -1:
                    if dp[i] == -1 or dp[i] > dp[i-coins[j]] + 1:
                        dp[i] = dp[i-coins[j]] + 1
        return dp[amount]