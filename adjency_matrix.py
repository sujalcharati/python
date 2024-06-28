# how to convert the given edges to form graph in adjacency matrix
def adi_mat(edges):
    vertices = max(max(u, v) for u, v in edges) + 1# no of nodes
    
    adj_matrix = [[0] * vertices for _ in range(vertices)]#2d array
    for u, v in edges:
        adj_matrix[u][v] = 1
        adj_matrix[v][u] = 1
    return adj_matrix

edges = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6),
         (3, 7), (4, 8), (5, 9), (6, 7), (7, 8), (8, 9)]

adj_matrix = adi_mat(edges)
print("Adjacency Matrix:")
for row in adj_matrix:
    print(row)  