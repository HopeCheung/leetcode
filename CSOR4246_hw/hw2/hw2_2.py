B='B'
A='A'
D='D'
G='G'
E='E'
C='C'
F='F'
G = {A:{B:5, C:10, D:3}, B:{A:5, E:10}, C:{A:10, E:5}, D:{A:3, E:12}, E:{B:10, C:5, D:12}}

def dijkstra(G, s, INF = 999):
    book = set(s)
    minv = s
    dis = {node:INF for node in G}
    p_num = {node:0 for node in G}
    p_num[s], dis[s] = 1, 0

    while len(book) < len(G):
        book.add(minv)
        for node in G[minv]:
            if dis[minv] + G[minv][node] < dis[node]:
                dis[node] = dis[minv] + G[minv][node]
                p_num[node] = p_num[minv]
            elif dis[minv] + G[minv][node] == dis[node]:
            	p_num[node] = p_num[node] + p_num[minv]
        new = INF
        for v in dis.keys():
            if v in book:
                continue
            if dis[v] < new:
                new = dis[v]
                minv = v
    return p_num
