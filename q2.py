import math

class Vertex:
    def __init__(self, name):
        self.name = name
        self.edges = []  # list of edges connected to this vertex

    def __str__(self):
        return self.name


class Edge:
    def __init__(self, source, target, capacity):
        self.source = source
        self.target = target
        self.capacity = capacity
        self.flow = 0

    def __str__(self):
        return f"{self.source} -> {self.target} | Capacity: {self.capacity} | Flow: {self.flow}"


class Network:
    def __init__(self):
        self.vertices = []

    def add_vertex(self, name):
        vertex = Vertex(name)
        self.vertices.append(vertex)
        return vertex

    def add_edge(self, source, target, capacity):
        edge = Edge(source, target, capacity)
        source.edges.append(edge)
        return edge

    def __str__(self):
        result = "Network:\n"
        for v in self.vertices:
            result += f"Vertex: {v}\n"
            for e in v.edges:
                result += f"  {e}\n"
        return result

    def make_network(self, preferences, licenses):
        # Create source and sink vertices
        source = self.add_vertex("source")
        sink = self.add_vertex("sink")

        # Create p vertices and connect them to source
        p_vertices = [self.add_vertex(f"p{i}") for i in range(len(preferences))]
        for p_vertex in p_vertices:
            self.add_edge(source, p_vertex, 1)

        # Create d vertices
        num_d_vertices = math.ceil(len(preferences) / 5)
        d_vertices = [self.add_vertex(f"d{i}") for i in range(num_d_vertices)]

        # Create c vertices
        num_c_vertices = math.ceil(len(preferences) / 5)
        c_vertices = [self.add_vertex(f"c{i}") for i in range(num_c_vertices)]

        # Connect p vertices with d and c vertices based on preferences
        for i, p_vertex in enumerate(p_vertices):
            for pref in preferences[i]:
                # Connect to c vertices
                self.add_edge(p_vertex, c_vertices[pref], 1)
                # Connect licensed p vertices to d vertices
                if i in licenses:
                    self.add_edge(p_vertex, d_vertices[pref], 1)

        # Connect d vertices to sink with capacity 2
        for d_vertex in d_vertices:
            self.add_edge(d_vertex, sink, 2)

        # Connect c vertices to sink with capacity 3
        for c_vertex in c_vertices:
            self.add_edge(c_vertex, sink, 3)

class ResidualNetwork(Network):

    def __init__(self,network):
        super().__init__()

    def bfs(self, source, sink, parent):
        visited = [False] * len(self.vertices)
        queue = []
        queue.append(source)
        visited[self.vertices.index(source)] = True

        while queue:
            u = queue.pop(0)

            for edge in u.edges:
                v = edge.target
                if (not visited[self.vertices.index(v)]) and (edge.capacity - edge.flow > 0):
                    queue.append(v)
                    visited[self.vertices.index(v)] = True
                    parent[self.vertices.index(v)] = u

        return visited[self.vertices.index(sink)]

    def ford_fulkerson(self, source, sink):
        parent = [-1] * len(self.vertices)
        max_flow = 0

        while self.bfs(source, sink, parent):
            path_flow = float("inf")
            s = sink

            while s != source:
                u = parent[self.vertices.index(s)]
                for edge in u.edges:
                    if edge.target == s:
                        path_flow = min(path_flow, edge.capacity - edge.flow)
                        break
                s = u

            max_flow += path_flow
            v = sink

            while v != source:
                u = parent[self.vertices.index(v)]
                for edge in u.edges:
                    if edge.target == v:
                        edge.flow += path_flow
                        break
                v = u

        return max_flow

    def __str__(self):
        return super().__str__()

if __name__ == '__main__':
    preferences = [[0], [1], [0, 1], [0, 1], [1, 0], [1], [1, 0], [0, 1], [1]]
    licences = [1, 4, 0, 5, 8]
    network=Network()
    network.make_network(preferences, licences)
    print(network)
    residual=ResidualNetwork(network)
    print(residual)

