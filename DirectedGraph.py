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

addEdge(graph,'1','2')
addEdge(graph,'1','3')
addEdge(graph,'2','4')
addEdge(graph,'2','5')
addEdge(graph,'3','1')
addEdge(graph,'3','5')
addEdge(graph,'4','2')
addEdge(graph,'5','2')
addEdge(graph,'5','3')


pathCollection = generate_edges(graph)

print(pathCollection)
print(graph)

# detecting f a graph has a cycle with DFS
def dfs(graph, start, end):
    stack = [(start, [])]
    while stack:
        currentNode, path = stack.pop()
        if path and currentNode == end:
            yield path
            continue
        for next_neighbour in graph[currentNode]:
            if next_neighbour in path:
                continue
            stack.append((next_neighbour, path+[next_neighbour]))

for node in graph:
    for path in dfs(graph, node, node):
        cycles = [node] + path
        print(cycles)





