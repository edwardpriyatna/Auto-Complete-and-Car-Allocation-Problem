import math

class Vertex:
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.parent=None

    def __str__(self):
        return self.name

class Edge:
    def __init__(self, start_vertex, end_vertex, capacity, flow=0):
        self.start_vertex = start_vertex
        self.end_vertex = end_vertex
        self.capacity = capacity
        self.flow = flow

    def __str__(self):
        return f"{self.start_vertex} -> {self.end_vertex} : {self.flow}/{self.capacity}"

class NetworkFlow:
    def __init__(self):
        self.vertices = []
        self.edges = []

    def add_vertex(self, vertex):
        self.vertices.append(vertex)

    def add_edge(self, edge):
        self.edges.append(edge)

    def __str__(self):
        return "\n".join(str(edge) for edge in self.edges)

    def make_network(self, preferences, licenses):
        # Create vertices
        source1 = Vertex('source1')
        source2 = Vertex('source2')
        sink = Vertex('sink')
        p_vertices = [Vertex(f'p{i}') for i in range(len(preferences))]
        d_vertices = [Vertex(f'd{i}') for i in range(math.ceil(len(preferences) / 5))]
        c_vertices = [Vertex(f'c{i}') for i in range(math.ceil(len(preferences) / 5))]

        # Add vertices to network
        for vertex in [source1, source2] + p_vertices + d_vertices + c_vertices + [sink]:
            self.add_vertex(vertex)

        # Add edge from source1 to source2
        self.add_edge(Edge(source1, source2, len(preferences)))

        # Add edges from source2 to p_vertices
        for p_vertex in p_vertices:
            self.add_edge(Edge(source2, p_vertex, 1))

        # Add edges from licensed p_vertices to d_vertices
        for license in licenses:
            for preference in preferences[license]:
                self.add_edge(Edge(p_vertices[license], d_vertices[preference], 1))

        # Add edges from d_vertices to sink
        for d_vertex in d_vertices:
            self.add_edge(Edge(d_vertex, sink, 2))

        # Add edges from p_vertices to c_vertices
        for i, preference in enumerate(preferences):
            for pref in preference:
                self.add_edge(Edge(p_vertices[i], c_vertices[pref], 1))

        # Add edges from c_vertices to sink
        for c_vertex in c_vertices:
            self.add_edge(Edge(c_vertex, sink, 3))

class ResidualNetwork(NetworkFlow):
    def __init__(self, network):
        super().__init__()
        self.vertices = network.vertices
        self.edges = [Edge(edge.start_vertex, edge.end_vertex, edge.capacity, edge.flow) for edge in network.edges]

    def has_AugmentingPath(self, source, sink):
        # This is a simple BFS to check if there is a path from source to sink
        for vertex in self.vertices:
            vertex.visited = False
            vertex.parent = None
        queue = [source]
        source.visited = True

        while queue:
            vertex = queue.pop(0)
            for edge in self.edges:
                residual_capacity = edge.capacity - edge.flow
                if edge.start_vertex == vertex and not edge.end_vertex.visited and residual_capacity > 0:
                    edge.end_vertex.parent = edge
                    if edge.end_vertex == sink:
                        return True
                    queue.append(edge.end_vertex)
                    edge.end_vertex.visited = True
        return False

    def get_AugmentingPath(self, source, sink):
        # This method should return the augmenting path as a list of edges
        path = []
        current_vertex = sink
        while current_vertex != source:
            edge = current_vertex.parent
            path.append(edge)
            current_vertex = edge.start_vertex
        path.reverse()
        return path

    def augment_flow(self, path):
        # This method should update the flow in the residual network based on the augmenting path
        min_residual_capacity = min(edge.capacity - edge.flow for edge in path)
        for edge in path:
            edge.flow += min_residual_capacity

    def ford_fulkerson(self):
        flow = 0
        while self.has_AugmentingPath(self.vertices[0], self.vertices[-1]):
            path = self.get_AugmentingPath(self.vertices[0], self.vertices[-1])
            min_residual_capacity = min(edge.capacity - edge.flow for edge in path)
            flow += min_residual_capacity
            self.augment_flow(path)
        return flow

    def get_connected_vertices(self):
        connected_vertices = []
        d_vertices = [vertex for vertex in self.vertices if vertex.name.startswith('d')]
        c_vertices = [vertex for vertex in self.vertices if vertex.name.startswith('c')]

        for d_vertex, c_vertex in zip(d_vertices, c_vertices):
            p_vertices_d = [edge.start_vertex.name for edge in self.edges if
                            edge.end_vertex == d_vertex and edge.flow > 0]
            p_vertices_c = [edge.start_vertex.name for edge in self.edges if
                            edge.end_vertex == c_vertex and edge.flow > 0]
            connected_vertices.append([p_vertices_d, p_vertices_c])

        return connected_vertices

def allocate(preferences, licenses):
    networkFlow=NetworkFlow()
    networkFlow.make_network(preferences,licenses)
    residual=ResidualNetwork(networkFlow)
    print(residual)
    residual.ford_fulkerson()
    print(residual)
    output=residual.get_connected_vertices()
    return output

if __name__ == '__main__':
    preferences = [[0], [1], [0, 1], [0, 1], [1, 0], [1], [1, 0], [0, 1], [1]]
    licences = [1, 4, 0, 5, 8]
    print(allocate(preferences, licences))



