class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        if envelopes == []:
            return 0
        
        envelopes, N = sorted(envelopes), len(envelopes)
        dp = [0] * N
        dp[0] = 1
        
        for i in range(1, len(envelopes)):
            check = [dp[j] + 1 for j in range(i) if envelopes[i][0] > envelopes[j][0] and envelopes[i][1] > envelopes[j][1]]
            if check == []:
                dp[i] = 1
            else:
                dp[i] = max(check)
        return max(dp)
        
#-------DP------TLE-----------------------
class Solution2(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        def binary_search(target, lst):
            left, right = 0, len(lst) - 1
            while left <= right:
                mid = (left + right) // 2
                if lst[mid] == target:
                    return mid
                elif lst[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left
        
        if envelopes == []:
            return 0
        
        envelopes.sort(
        cmp = lambda x, y: x[0] - y[0] if x[0] != y[0] else y[1] - x[1]) 
        widths = [elem[1] for elem in envelopes]
        res = []
        
        for width in widths:
            pos = binary_search(width, res)
            if pos >= len(res):
                res.append(width)
            else:
                res[pos] = width
                
        return len(res)
#------greedy + binary_search
