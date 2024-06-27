edges = [(0, 1,4), (0, 2,5), (1, 3,8), (1, 4,6), (2, 5,3), (2, 6,7),
         (3, 7,5), (4, 8,4), (5, 8,6), (7,9,8 ), (8, 9,3),(6,10,5),(7,11,7),(8,10,5)]

class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = adi_mat(edges)# function call from another file

    def printMST(self, parent):
        print("Edge \tWeight")
        for i in range(1, self.V):
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]])

    def minKey(self, key, mstSet):
        min = float("inf")
        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v

        return min_index

    def primMST(self):
        key = [float("inf")] * self.V
        parent = [None] * self.V
        key[0] = 0
        mstSet = [False] * self.V

        for cout in range(self.V):
            u = self.minKey(key, mstSet)
            mstSet[u] = True
            for v in range(self.V):
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        self.printMST(parent)

g = Graph(len(adj_matrix))



g.primMST()
