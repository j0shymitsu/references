class Graph:
    def _init__(self, num_vertices):
        self.graph = {}
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
    
    def adjacent_nodes(self, node):
        return self.graph[node]
    
    def unconnected_vertices(self):
        no_connections = []
        for key in self.graph.keys():
            if self.graph[key] == set():
                no_connections.append(key)
        return no_connections
    

class GraphAdjList:
    ''' 
    Adjacency list: The node's list will not contain a reference to nodes that
    it doesn't share an edge with
    '''
    def _init__(self):
        self.graph = {}

    def add_edge(self, v, u):
        if u not in self.graph.keys():
            self.graph[u] = {v}
        if v not in self.graph.keys():
            self.graph[v] = {u}
        if u in self.graph.keys():
            self.graph[u].add(v)
        if v in self.graph.keys():
            self.graph[v].add(u)

    def edge_exists(self, u, v):
        if u in self.graph and v in self.graph:
            return (v in self.graph[u]) and (u in self.graph[v])
        return False