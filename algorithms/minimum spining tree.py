class Graph(object):
    def __init__(self,maps):
        self.maps = maps
        self.node_num = self.get_node()
        self.edge_num = self.get_edge()
        
    def get_node():
        return len(self.maps)
    
    def get_edge():
        count = 0
        for i in range(self.node_num):
            for j in range(i):
                if self.maps[i][j] > 0 and self.maps[i][j] <9999:
                    count = count + 1
        return count

    def kruskal(self):
        res = []
        if self.node_num <= 0 or self.edge_num < self.node_num - 1:
            return res
        edge_list = []
        for i in range(self.node_num):
            for j in range(i, self.node_num):
                if self.maps[i][j] < 9999:
                    edge_list.append([i, j, self.maps[i][j]])
        edge_list.sort(key=lambda a: a[2])

        group = [[i] for i in range(self.node_num)]
        for edge in edge_list:
            for i in range(len(group)):
                if edge[0] in group[i]:
                    m = i                             #start point
                if edge[1] in group[i]:
                    n = i                             #end point
            if m != n:
                res.append(edge)                      #add edge
                group[m] = group[m] + group[n]
                group[n] = []
        return res

    def prime(self):
        res = []
        if self.node_num <= 0 or self.edge_num < self.node_num - 1:
            return res
        res = []
        selected_node = [0]
        candidate_node = [i for i in range(1, self.node_num)]
        while len(candidate_node) > 0:
            begin, end, minweight = 0, 0, 9999
            for i in selected_node:
                for j in candidate_node:
                    if self.maps[i][j] < minweight:
                        minweight = self.maps[i][j]
                        begin = i
                        end = j
            res.append([begin, end, minweight])
            selected_node.append(end)
            candidate_node.remove(end)
        return res
            
