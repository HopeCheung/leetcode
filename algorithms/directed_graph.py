class directedgraph(object):
    def __init__(self, d):
        if isinstance(d,dict):
            self.graph = d
        else:
            self.graph = dict()
            print('Error')

    def generatePath(self, graph, path, end, results):
        current = path[-1]
        if current == end:
            results.append(path)
        else:
            for n in graph[current]:
                if n not in path:
                    self.generatePath(graph, path+[n], end, results)

    def searchPath(self, start, end):
        self.results = []
        self.generatePath(self.graph, [start], end, self.results)
        for path in self.results:
            print(path)
