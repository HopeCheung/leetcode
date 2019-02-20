class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        def helper(a, b):
            if a == 0 or a == 1:
                return a
            if b == 0:
                return 1
            if b == 1:
                return a % 1337
            
            if b % 2 == 0:
                divide = helper(a, b//2)
                return (divide * divide) % 1337
            else:
                divide = helper(a, b//2)
                return (a * divide * divide) % 1337
            
        a = a % 1337
        b = "".join(map(str, b))
        return helper(a, int(b))
    
        