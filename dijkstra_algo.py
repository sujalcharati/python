# dijikstra
def dijkstra(edges, vertices, source):
    distances = [float('inf')] * vertices
    visited = [False] * vertices
    parent = [0] * vertices
    distances[source] = 0
    for v in range(vertices):
        u = -1
        for i in range(vertices):
            if not visited[i] and (u == -1 or distances[i] < distances[u]):
                u = i
        visited[u] = True #visited
        for edge in edges:
            if edge[0] == u:# initialising (u,v,w) analogy to edges
                v = edge[1]
                weight = edge[2]
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
                    parent[v] = u
    print("Vertex   Distance from Source")
    for i in range(vertices):
        print(f"{i}\t\t{distances[i]}")
    print("\nShortest Path :")
    for i in range(vertices):
        print(f"{i} : {parent[i]}")
edges = [(0, 1, 4), (0, 2, 5), (1, 3, 8), (1, 4, 6), (2, 5, 3), (2, 6, 7), (3, 7, 5), (4, 8, 4), (5, 8, 6), (7, 9, 8), (8, 9, 3), (6, 10, 5),(7, 11, 7), (8, 10, 5)]
vertices = 12
source = 0
dijkstra(edges, vertices, source)# function call