class Solution:
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        if n == 1:
            return 1
        
        res, pri = [1], [0] * len(primes)
        for i in range(n-1):
            min_num = min([res[pri[k]] * primes[k] for k in range(len(primes))])
            res.append(min_num)
            for j in range(len(primes)):
                if res[pri[j]] * primes[j] == min_num:
                    pri[j] = pri[j] + 1
        return res[-1]
        
            
                
            
            
                
        
        