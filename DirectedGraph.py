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
addEdge(graph,'2','3')
addEdge(graph,'3','1')

pathCollection = generate_edges(graph)

print(pathCollection)
print(graph)

# detecting f a graph has a cycle with DFS
def dfs(graph, start, end):
    fringe = [(start, [])]
    while fringe:
        state, path = fringe.pop()
        if path and state == end:
            yield path
            continue
        for next_state in graph[state]:
            if next_state in path:
                continue
            fringe.append((next_state, path+[next_state]))

for node in graph:
    for path in dfs(graph, node, node):
        cycles = [node] + path
        print(cycles)



