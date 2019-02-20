class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        if n == 0:
            return 1
        if n == 1:
            return 10
        ans = 10
        val = 9
        for i in range(2, n + 1):
            val = val * (9 - i + 2)
            ans = ans + val
        return ans