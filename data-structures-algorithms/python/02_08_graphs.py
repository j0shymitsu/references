class Graph:
    def _init__(self, num_vertices):
        self.graph = []
        for i in range(0, num_vertices):
            new_graph = [False] * num_vertices
            self.graph.append(new_graph)

    def add_edge(self, v, u):
        self.graph[u][v] = True
        self.graph[v][u] = True

    def edge_exists(self, u, v):
        if u < 0 or u >= len(self.graph):
            return False
        if len(self.graph) == 0:
            return False
        row1 = self.graph[0]
        if v < 0 or v >= len(row1):
            return False
        return self.graph[u][v]