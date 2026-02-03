class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph.keys():
            self.graph[u].add(v)
        else:
            self.graph[u] = set([v])
        if v in self.graph.keys():
            self.graph[v].add(u)
        else:
            self.graph[v] = set([u])

    def breadth_first_search(self, v):
        visited = []
        queue = []
        queue.append(v)
        while queue:
            vertex = queue.pop(0)
            visited.append(vertex)
            neighbours = sorted(self.graph[vertex])
            for neighbour in neighbours:
                if neighbour not in visited and neighbour not in queue:
                    queue.append(neighbour)
        return visited
    
    def depth_first_search(self, start_vertex):
        visited = []
        self.depth_first_search_r(visited, start_vertex)
        return visited

    def depth_first_search_r(self, visited, current_vertex):
        visited.append(current_vertex)
        neighbours = sorted(self.graph[current_vertex])
        for neighbour in neighbours:
            if neighbour not in visited:
                self.depth_first_search_r(visited, neighbour)

    def __repr__(self):
        result = ""
        for key in self.graph.keys():
            result += f"Vertex: '{key}'\n"
            for v in sorted(self.graph[key]):
                result += f"has an edge leading to --> {v} \n"
        return result