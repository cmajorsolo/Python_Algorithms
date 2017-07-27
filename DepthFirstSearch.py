graph = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']}
################################  DFS ###########################
def dfs(graph, start):
    visited, stack = [], [start]
    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            newList = list(set(graph[n]) - set(visited))
            stack  = stack + newList
    return visited

print (dfs(graph, 'A'))


################################  DFS PRINT PATH ###########################
def dfs_paths(graph, start, goal, path=None):
    if path is None:
        path = [start]
    if start == goal:
        yield path
    for next in list(set(graph[start]) - set(path)):
        yield from dfs_paths(graph, next, goal, path + [next])

print (list(dfs_paths(graph, 'C', 'F')))

################################  BFS ###########################
def bfs(graph, start):
    visited, queue = [], [start]
    while queue:
        n = queue.pop(0)
        if n not in visited:
            visited.append(n)
            newList= list(set(graph[n]) - set(visited))
            queue += newList
    return visited
print(bfs(graph, 'A'))

################################  DFS PRINT PATH ###########################
def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        vertex, path = queue.pop()
        for next in list(set(graph[vertex]) - set(path)):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path+[next]))
print(list(bfs_paths(graph, 'A', 'F')))

################################  SHORTEST DFS PRINT PATH ###########################
def shortest_path(graph, start, goal):
    try:
        return next(bfs_paths(graph, start, goal))
    except StopIteration:
        return None

shortest_path(graph, 'A', 'F')