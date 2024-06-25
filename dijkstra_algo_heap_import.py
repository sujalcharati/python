import heapq

def dijkstra(G, start):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    previous = {vertex: None for vertex in graph}
    queue = [(0, start)]

    while queue:
        current_distance, current_vertex = heapq.heappop(queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_vertex
                heapq.heappush(queue, (distance, neighbor))

    return distances, previous


graph = {
    0: {1: 4, 2: 5},
    1: {3: 8, 4: 6},
    2: {5: 3, 6: 7},
    3: {7: 5},
    4: {8: 4},
    5: {8: 6},
    6: {10: 5},
    7: {9: 8, 11: 7},
    8: {9: 3, 10: 5},
    9: {},
    10: {},
    11: {}
}

start_vertex = 0
distances, previous = dijkstra(graph, start_vertex)

print("Distances from vertex", start_vertex, ":")
for vertex, distance in distances.items():
    print("Vertex", vertex, ":", distance)

print("\nPrevious vertices in shortest paths:")
for vertex, prev in previous.items():
    print("Vertex", vertex, ":", prev)