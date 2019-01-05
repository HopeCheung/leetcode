graph = {
    0:set([1]),
    1:set([3]),
    2:set([1, 4]),
    3:set([0]),
    4:set([2, 5]),
    5:set([])
}
def tarjan(graph):
    #input: graph G = (V, E)
    #output: Array of strongly connected components (sets of vertices)
    n = len(graph)
    sccs = []
    index = [0]
    indexes = [-1] * n
    lows = [float('Inf')] * n
    S = []

    def strongconnect(v):
        # Set the depth index for v to the smallest unused index
        indexes[v] = index[0]
        lows[v] = index[0]
        index[0] += 1
        S.append(v)

        # Consider successors of v
        for chld in graph[v]:
            if indexes[chld] == -1:
                # Successor chld has not yet been visited; recurse on it
                strongconnect(chld)
                lows[v] = min(lows[v], lows[chld])
            elif chld in S:
                # Successor w is in stack S and hence in the current SCC
                lows[v] = min(lows[v], lows[chld])

        # If v is a root node, pop the stack and generate an SCC
        if lows[v] == indexes[v]:
            scc = set([v])
            w = S.pop()
            while w != v:
                scc.add(w)
                w = S.pop()
            sccs.append(scc)

    for v in graph.keys():
        if indexes[v] == -1:
            strongconnect(v)

    return sccs
