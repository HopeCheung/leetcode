graph = {1:[2,4,5], 2:[1,3,4], 3:[2,4,5], 4:[1,2,3,5], 5:[1,3,4]}

def path_num(graph, v, w):
    visited = {node:False for node in graph}
    result = []

    def dfs(graph, v, w, path):
        if v == w:
            result.append(len(path))
            return
        visited[v] = True
        for node in graph[v]:
            if not visited[node]:
            	if node not in path:
                	visited[node] = True
                	path.append(node)
                	dfs(graph, node, w, path)
                	visited[node] = False
                	path.pop()
    dfs(graph,v,w,[v])
    return len([elem for elem in result if elem == min(result)])
path_num(graph, 1,3)
'''
def find_paths(graph, v, w, path = []):
	path = path + [v]
	if v not in graph:
		return []
	if v == w:
		return [path]
	paths = []
	for node in graph[v]:
		if node not in path:
			newpaths = find_paths(graph, v, w, path)
			for newpath in newpaths:
				paths.append(newpath)
	return paths
	'''