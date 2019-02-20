class Solution:
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1:
            return [0]
        
        graph = [[] for i in range(n)]
        degree = [0] * n
        for i in range(len(edges)):
            graph[edges[i][0]].append(edges[i][1])
            graph[edges[i][1]].append(edges[i][0])
            degree[edges[i][0]] += 1
            degree[edges[i][1]] += 1
            
        nodes, leaves = n, [i for i in range(n) if degree[i] == 1]
        while nodes > 2:
            new_leaves = []
            for i in leaves:
                degree[i], nodes = 0, nodes - 1
                for j in graph[i]:
                    degree[j] -= 1
                    if degree[j] == 1:
                        new_leaves.append(j)
            leaves = new_leaves
        return leaves
#---------topological sort-------------------------------------------