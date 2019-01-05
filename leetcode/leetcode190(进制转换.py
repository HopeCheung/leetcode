class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        result = bin(n)[2:] #十进制转二进制
        result = (32-len(result)) * '0' + result
        result = result[::-1]
        result = int(result, 2) #二进制转十进制（注意，2替换为8则是八进制转十进制）
        return result
