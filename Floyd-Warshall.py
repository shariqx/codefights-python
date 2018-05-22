def efficientRoadNetwork(n, roads):
    V = 0
    V = n
    graph = [[4] * n for x in range(V)]
    for i in range(V):
        graph[i][i] = 0
    for x,y in roads:
        graph[x][y] = 1
        graph[y][x] = 1
    return floydWarshall(graph,V)


def floydWarshall(graph, V):
    dist = graph

    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][j]  > dist[i][k]+ dist[k][j]:
                    dist[i][j] = min(dist[i][j] ,
                                      dist[i][k]+ dist[k][j])

    printSolution(dist, V)
    for i in range(V):
        for j in range(V):
            if dist[i][j] >=3:
                return False
    return True

def printSolution(dist, V):
    INF = -1
    for i in range(V):
        for j in range(V):
            if(dist[i][j] == INF):
                print("%7s" %("INF"), end = '')
            else:
                print("%7d\t" %(dist[i][j]),end = '')
            if j == V-1:
                print("")


roads = [
        [0,1],
    [0,3],
    [3,2],
    [0,2],
]
print(efficientRoadNetwork(4,roads))