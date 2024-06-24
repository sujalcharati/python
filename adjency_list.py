def adi_list(edges):
    adj_list = {}
    for u, v in edges:
        if u not in adj_list:
            adj_list[u] = []
        if v not in adj_list:
            adj_list[v] = []
        adj_list[u].append(v)
        adj_list[v].append(u)
    return adj_list

edges = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6),
         (3, 7), (4, 8), (5, 9), (6, 7), (7, 8), (8, 9)]

adj_list = adi_list(edges)
print("\nAdjacency List:")
for vertex in adj_list:
    print(f"{vertex}: {adj_list[vertex]}")