from collections import defaultdict

graph = defaultdict(list)

def addEdge(graph, u, v):
    graph[u].append(v)

def generate_edges(graph):
    edges = []
    for node in graph:
        for neigbours in graph[node]:
            edges.append((node, neigbours))

    return edges

addEdge(graph,'a','c')
addEdge(graph,'b','c')
addEdge(graph,'b','e')
addEdge(graph,'c','d')
addEdge(graph,'c','e')
addEdge(graph,'c','a')
addEdge(graph,'c','b')
addEdge(graph,'e','b')
addEdge(graph,'d','c')
addEdge(graph,'d','a')
addEdge(graph,'e','c')

pathCollection = generate_edges(graph)

print(pathCollection)
print(graph)

