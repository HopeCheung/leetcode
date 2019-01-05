class graph(object):
	def _init__(self, *args, **kwargs):
                self.node_neighbors = {}
                self.visited = {}

        def add_nodes(self, nodelist):
                for node in nodelist:
                        self.add_node(node)

        def add_node(self, node):
                if not node in self.nodes():
                        self.node_neighbors[node] = []

        def add_edge(self, edge):
                u, v = edge
                if (v not in self.node_neighbors[u]) ad (u not in self.node_neighbors[v]):
                        self.node_neighbors[u].append(v)
                        if u != v:
                                self.node_neighbors[v].append(u)

        def nodes(self):
                return self.node_neighbors.keys()

        def depth_first_search(self, root = None):
                order = []
                def dfs(node):
                        self.visited[node] = True
                        order.append(node)
                        for n in self.node_neighbors[node]:
                                if not n in self.visited:
                                        dfs(n)
                if root:
                        dfs(root)
                for node in self.nodes():
                        if not node in self.visited:
                                dfs(node)
                return order

        def breadth_first_search(self, root = None):
                queue = []
                order = []
                def bfs():
                        while len(queue) > 0:
                                node = queue.pop(0)
                                self.visited[node] = True
                                for n in self.node_neighbors[node]:
                                        if (not n in self.visited) and (not n in queue):
                                                queue.append(n)
                                                order.append(n)

                if root:
                        queue.append(root)
                        order.append(root)
                        bfs()
                for node in self.nodes():
                        if not node in self.visited:
                                queue.append(node)
                                order.append(node)
                                bfs()
                return order

        def find_path(self, start, end, path=[]):
                path = path + [start]
                if start == end:
                        return path
                if not start in self.nodes():
                        return None
                for node in self.node_neighbors[start]:
                        if not node in path:
                                newpath = self.find_path(node, end, path)
                                if newpath:
                                        return newpath
                return None

        def find_all_paths(start, end, path=[]):
                path = path + [start]
                if not start in self.nodes():
                        return []
                if start == end:
                        return [path]
                paths = []
                for node in self.neighbors[start]:
                        if node not in path:
                                newpaths = self.find_all_paths(node, end, path)
                                for newpath in newpaths:
                                        paths.append(newpath)
                return paths

        def find_shortest_path(start, end, path = []):
                path = path + [start]
                if start == end:
                        return path
                if not start in self.nodes():
                        return None
                shortest = None
                for node in self.neighbors[start]:
                        if node not in path:
                                newpath = find_shortest_path(node, end, path)
                                if newpath:
                                        if not shortest or len(newpath) < len(shortest):
                                                shortest = newpath
                return shortest
                                
        
