import collections

def bfs(graph, root):
    seen, queue = set([root]), collections.deque([root])
    node_vs_visitables = {}
    while queue:
        vertex = queue.popleft()
        visit(vertex)
        hop = 0
        if not graph.get(vertex):
            continue
        for node in graph[vertex]:
            if node not in seen:
                seen.add(node)
                queue.append(node)  

def visit(n):
    print(n)

if __name__ == '__main__':
    roads = [[3, 0], [0, 4], [5, 0], [2, 1],
          [1, 4], [2, 3], [5, 2]]
    graph = {}
    for i in range(0, len(roads)):
        if graph.get(roads[i][0]):
            graph[roads[i][0]].append(roads[i][1])
        else:
            graph[roads[i][0]] = []
            graph[roads[i][0]].append(roads[i][1])
        if graph.get(roads[i][1]):
            graph[roads[i][1]].append(roads[i][0])
        else:
            graph[roads[i][1]] = []
            graph[roads[i][1]].append(roads[i][0])
    print(graph)
    bfs(graph, 4)