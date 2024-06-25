def bfs_tree(g, v):
    marked = [False] * len(g)
    queue = [v]
    tree_edges = []
    marked[v] = True

    while queue:
        v = queue.pop(0)
        for u in g.get(v, []):
            if not marked[u]:
                marked[u] = True
                queue.append(u)
                tree_edges.append((v, u))

    return tree_edges

g = {
    0: [1, 2],
    1: [3],
    2: [3, 5],
    3: [4, 5],
    4: [5],
    5: []
}


tree_edges = bfs_tree(g, 0)
print("BFS Tree Edges:", tree_edges)