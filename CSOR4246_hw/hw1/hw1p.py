import networkx 
import urllib2
homer = urllib2.urlopen('http://people.sc.fsu.edu/~jburkardt/datasets/sgb/homer.dat')

def read_nodes(gfile):
    def node_name(line):
        line_splitted = line.split(' ')    #split the line with ' '
        return line_splitted[0].strip()    #return first word
    lst = []
    for line in gfile:
        if line.startswith('*'):           #comment line, we ignore it
            continue
        elif len(line.strip()) == 0:       #blank line, means comes to the end
            break
        else:
            yield node_name(line) #append node in the lst


def read_edges(gfile):
    def target_line(line):
        first = line.split(':')[0]
        if first == '&' or first.isdigit():
            return True
        return False
    
    def groups(line):
        edge_groups = line.split(':')[1].strip()
        lst = []
        for edge in edge_groups.split(';'):
            lst.append(edge.split(','))
        return lst

    def combine(group):
        for i in range(len(group)):
            for j in range(i+1, len(group)):
                yield (group[i], group[j])
        
    for line in gfile:
        if not target_line(line):
            continue
        for group in groups(line):
            for pair in combine(group):
                yield pair
    pass


import networkx as nx
G = nx.Graph()
G.add_nodes_from(read_nodes(homer))
G.add_edges_from(read_edges(homer))

def Search(graph, root):
    visited = {node:False for node in graph.nodes}
    result = []
    
    def dfs(graph, root):
        for node in sorted(graph.neighbors(root)): 
            if not visited[node]:
                visited[node] = True
                result.append(node)
                dfs(graph, node)
                
    visited[root] = True
    result.append(root)
    dfs(graph, root)
    return result
    pass

ulysses = Search(G, 'OD')

def connected_components(graph):
    visited = {node:False for node in graph.nodes}
    components = []

    def search(graph, root):
        result = [] 
        def dfs(graph, root):
            for node in sorted(graph.neighbors(root)): 
                if not visited[node]:
                    visited[node] = True
                    result.append(node)
                    dfs(graph, node)           
        visited[root] = True
        result.append(root)
        dfs(graph, root)
        return result
    
    def find_connect(graph):
        for node in sorted(graph.nodes):
            if not visited[node]:
                components.append(search(graph, node))
    find_connect(graph)
    return components
    pass

character_interactions = connected_components(G)
component_sizes = [len(c) for c in character_interactions]
print "There are 12 connected components in the Iliad:", len(component_sizes) == 12
print "The giant component has size 542:", max(component_sizes) == 542
print "There are 5 isolated characters:", len([c for c in component_sizes if c == 1]) == 5


