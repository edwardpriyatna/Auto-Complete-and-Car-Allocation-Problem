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
        self.edges=[]

    def add_vertex(self, name):
        vertex = Vertex(name)
        self.vertices.append(vertex)
        return vertex

    def add_edge(self, source, target, capacity):
        edge = Edge(source, target, capacity)
        source.edges.append(edge)
        self.edges.append(edge)
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

        # Connect p vertices with d vertices based on preferences and licenses
        for i, p_vertex in enumerate(p_vertices):
            if i in licenses:
                for pref in preferences[i]:
                    self.add_edge(p_vertex, d_vertices[pref], 1)

        # Create c vertices
        num_c_vertices = math.ceil(len(preferences) / 5)
        c_vertices = [self.add_vertex(f"c{i}") for i in range(num_c_vertices)]

        # Connect p vertices with c vertices based on preferences
        for i, p_vertex in enumerate(p_vertices):
            for pref in preferences[i]:
                self.add_edge(p_vertex, c_vertices[pref], 1)

        # Connect d vertices to sink with capacity 2
        for d_vertex in d_vertices:
            self.add_edge(d_vertex, sink, 2)

        # Connect c vertices to sink with capacity 3
        for c_vertex in c_vertices:
            self.add_edge(c_vertex, sink, 3)

class ResidualNetwork(Network):

    def __init__(self,network):
        super().__init__()
        self.vertices = network.vertices
        self.edges = network.edges

    def __str__(self):
        return super().__str__()

    def bfs(self, source, sink, parent):
        visited = [False] * len(self.vertices)
        queue = [source]
        visited[self.vertices.index(source)] = True

        while queue:
            u = queue.pop(0)  # pop from the beginning of the list

            for edge in u.edges:
                residual_capacity = edge.capacity - edge.flow
                if visited[self.vertices.index(edge.target)] == False and residual_capacity > 0:
                    queue.append(edge.target)
                    visited[self.vertices.index(edge.target)] = True
                    parent[self.vertices.index(edge.target)] = u

        return True if visited[self.vertices.index(sink)] else False

    def ford_fulkerson(self):
        source=self.vertices[0]
        sink=self.vertices[1]
        parent = [-1] * len(self.vertices)
        max_flow = 0

        while self.bfs(source, sink, parent):
            path_flow = float("Inf")
            s = sink
            while (s != source):
                for edge in self.edges:
                    if edge.target == s and edge.source == parent[self.vertices.index(s)]:
                        path_flow = min(path_flow, edge.capacity - edge.flow)
                        break
                s = parent[self.vertices.index(s)]

            max_flow += path_flow
            v = sink
            while (v != source):
                for edge in self.edges:
                    if edge.target == v and edge.source == parent[self.vertices.index(v)]:
                        edge.flow += path_flow
                        break
                v = parent[self.vertices.index(v)]
        return max_flow

    def get_connected_p_vertices(self):
        connected_p_vertices = []
        d_vertices = [v for v in self.vertices if v.name.startswith('d')]
        c_vertices = [v for v in self.vertices if v.name.startswith('c')]

        for d_vertex, c_vertex in zip(d_vertices, c_vertices):
            p_vertices_d = [int(edge.source.name[1:]) for edge in self.edges if
                            edge.target == d_vertex and edge.flow > 0 and edge.source.name.startswith('p')]
            p_vertices_c = [int(edge.source.name[1:]) for edge in self.edges if
                            edge.target == c_vertex and edge.flow > 0 and edge.source.name.startswith('p')]
            connected_p_vertices.append(p_vertices_d + p_vertices_c)
        return connected_p_vertices

def allocate(preferences,licenses):
    preferences=[sorted(sublist) for sublist in preferences]
    network=Network()
    network.make_network(preferences,licenses)
    residual=ResidualNetwork(network)
    max_flow= residual.ford_fulkerson()
    if max_flow<len(preferences):
        return None
    solution=residual.get_connected_p_vertices()
    print(solution)
    return solution

if __name__ == '__main__':
    preferences = [[0], [1], [0, 1], [0, 1], [1, 0], [1], [1, 0], [0, 1], [1]]
    licences = [1, 4, 0, 5, 8]
    print(allocate(preferences,licences))





