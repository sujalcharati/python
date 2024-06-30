def bellman_ford(graph, source):

    distances = {vertex: float('inf') for vertex in graph}# at initially the distance from the source to every node is considerd to be infinity as we do not know the actual distance.
    distances[source] = 0 # this distance is distance from source node to itself so distance is zero


    for _ in range(len(graph) - 1):
        for u in graph:
            for v, weight in graph[u].items():
                if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight#initialization of distance to its neigbours node 


    for u in graph:
        for v, weight in graph[u].items():# iteration is done to check the presence of negative cycle
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                raise ValueError("Graph contains negative weight cycle")

    return distances

graph = {
    'A': {'B': -1, 'C': 4},
    'B': {'C': 3, 'D': 2, 'E': 2},
    'C': {},
    'D': {'B': 1, 'C': 5},
    'E': {'D': -3}
}
source = 'A'

shortest_distances = bellman_ford(graph, source)#functon call
print(shortest_distances)
