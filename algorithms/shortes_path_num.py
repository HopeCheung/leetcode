graph = {1:[2, 3, 4], 2:[1, 5], 3:[1, 5], 4:[1, 6], 5:[2, 3, 7], 6:[4, 7], 7:[5, 6]}

def path_num(graph, v, w):
    queue = [v]
    s, p_num = {node:0 for node in graph}, {node:0 for node in graph}
    p_num[v] = 1
    while len(queue) != 0:
        start = queue[0]
        queue = queue[1:]
        dis = s[start] + 1
        for node in graph[start]:
            if (s[node] == 0 and node != v) or dis < s[node]:
                s[node] = dis
                p_num[node] = p_num[start]
                queue.append(node)
            elif s[node] == dis:
                p_num[node] = p_num[node] + p_num[start]
    return p_num[w]

path_num(graph, 1, 7)
#https://blog.csdn.net/basaowu/article/details/51249357