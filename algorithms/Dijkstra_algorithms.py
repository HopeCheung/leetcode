B='B'
A='A'
D='D'
G='G'
E='E'
C='C'
F='F'
G = {A:{B:5, C:10, D:3}, B:{A:5, D:2, E:10}, C:{A:10, E:5}, D:{A:3, B:2, E:12}, E:{B:10, C:5, D:12}}

def dijkstra(G, s, INF = 999):
    book = set(s)
    minv = s
    dis = {node:INF for node in G}
    step = {node:0 for node in G}
    dis[s] =  0

    while len(book) < len(G):
        book.add(minv)
        level = step[minv] + 1
        for node in G[minv]:
            if dis[minv] + G[minv][node] < dis[node]:
                dis[node] = dis[minv] + G[minv][node]
                step[node] = level
            elif dis[minv] + G[minv][node] == dis[node]:
                step[node] = min(step[node], level)
        new = INF
        for v in dis.keys():
            if v in book:
                continue
            if dis[v] < new:
                new = dis[v]
                minv = v
    return step
dijkstra(G, A)
