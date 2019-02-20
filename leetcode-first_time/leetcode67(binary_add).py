class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        def sumup(a, b, c):
            a, b, c = int(a), int(b), int(c)
            return str((a ^ b)  ^ c)
        
        def carry(a, b, c):
            a, b, c = int(a), int(b), int(c)
            return (a & b) | ((a | b) & c)
        
        s, c = [], 0
        while len(a) > 0 or len(b) > 0:
            if len(a) == 0:
                s, c = [sumup(0, b[len(b) - 1], c)] + s, carry(0, b[len(b) - 1], c)
                b = b[:len(b) - 1]
            elif len(b) == 0:
                s, c = [sumup(a[len(a) - 1], 0, c)] + s, carry(a[len(a) - 1], 0, c)
                a = a[:len(a) - 1]
            else:
                s, c = [sumup(a[len(a) - 1], b[len(b) - 1], c)] + s, carry(a[len(a) - 1], b[len(b) - 1], c)
                a, b = a[:len(a) - 1], b[:len(b) - 1]
        if c != 0:
            s = [str(c)] + s
        result = ''
        for elem in s:
            result = result + elem
        return result

