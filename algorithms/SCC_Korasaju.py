graph = {
    0:set([1]),
    1:set([3]),
    2:set([1, 4]),
    3:set([0]),
    4:set([2, 5]),
    5:set([])
}
def korasaju(graph):
	n = len(graph)
	visited = {node:False for node in graph}
	finish = []

	def dfs(graph, root):
		for node in graph[root]:
			if not visited[node]:
				visited[node] = True
				dfs(graph, node)
				finish.append(node)

	for node in graph:
		if not visited[node]:
			visited[node] = True
			dfs(graph, node)
			finish.append(node)
	
	finish = finish[::-1]
	new_graph = {}
	for node in graph:
		for elem in graph[node]:
			if elem not in new_graph:
				new_graph[elem] = set([node])
			else:
				new_graph[elem].add(node)

	new_visited = {node:False for node in new_graph}
	sccs = []
	def new_dfs(graph, root, scc):
		for node in graph[root]:
			if not new_visited[node]:
				new_visited[node] = True
				scc.add(node)
				new_dfs(graph, node, scc)
		return scc
				
		
	for node in finish:
		if not new_visited[node]:
			new_visited[node] = True
			scc = set([node])
			new_dfs(new_graph, node, scc)
			sccs.append(scc)
	return sccs


