class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        heap = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                heapq.heappush(heap, matrix[i][j])
        return heapq.nsmallest(k, heap)[-1]
        
class Solution2(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        heap = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if len(heap) == k:
                    heapq.heappushpop(heap, -matrix[i][j])
                else:
                    heapq.heappush(heap, -matrix[i][j])
        return -heapq.heappop(heap)

class Solution3(object):
    def kthSmallest(self, M, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        def toing(A, B,t):
            count = 0
            i = 0
            j = len(A[0])-1
            while i < len(A) and j>=0:
                if A[i][j] <= t:
                    i +=1
                    count += j+1
                    if count >= B:
                        return 1
                else:
                    j-=1
            return 0
        
        l = len(M)
        col = len(M[0])
        i = M[0][0] #min
        j = M[l-1][col-1]
        res = 0
        while i <= j:
            mid = i + (j - i) // 2
            #print (i,j, mid)
            if toing(M, k, mid):
                res = mid
                j = mid - 1
            else:
                i = mid + 1
        return res
    

