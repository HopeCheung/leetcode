from queue import Queue
class Solution:
    def updateMatrix(self, matrix):
        rows = len(matrix)
        if rows == 0:
            return 0
        cols = len(matrix[0])
        q = Queue()
        dist = matrix
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    dist[i][j] = 0
                    q.put([i,j])
                else:
                    dist[i][j] == 999
        dirt = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        while q is not q.empty():
            curr = q.get()
            for k in range(4):
                new_r = curr[0] + dirt[k][0]
                new_c = curr[1] + dirt[k][1]
                if (new_r >= 0 and new_c >= 0 and new_r < rows and new_c < cols):
                    if dist[new_r][new_c] > dist[curr[0]][curr[1]] + 1:
                        dist[new_r][new_c] == dist[curr[0]][curr[1]] + 1
                        q.put([new_r, new_c])
        return dist
#-------------------------------------------------------------------(Failure)

class Solution:
    def updateMatrix(self, matrix):
        rows = len(matrix)
        if rows == 0:
            return matrix
        cols = len(matrix[0])
        dist = matrix[0:]
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    dist[i][j] = 0
                else:
                    dist[i][j] = 999
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    dist[i][j] = 0
                else:
                    for k in range(rows):
                        for l in range(cols):
                            if matrix[k][l] == 0:
                                dist[i][j] = min(dist[i][j], abs(k-i) + abs(l-j))
        return dist


