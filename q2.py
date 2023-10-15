import math

class Vertex:
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.parent = None

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

        # Add vertices to the network
        for vertex in [source1, source2] + p_vertices + d_vertices + c_vertices + [sink]:
            self.add_vertex(vertex)

        # Add edge from source1 to source2
        self.add_edge(Edge(source1, source2, len(preferences)))

        # Add edges from source2 to p_vertices
        for p_vertex in p_vertices:
            self.add_edge(Edge(source2, p_vertex, 1))

        # Add edges from licensed p_vertices to d_vertices based on preferences
        for i, prefs in enumerate(preferences):
            if i in licenses:
                p_vertex = p_vertices[i]
                for pref in prefs:
                    d_vertex = d_vertices[pref]
                    self.add_edge(Edge(p_vertex, d_vertex, 1))

        # Add edges from d_vertices to sink
        for d_vertex in d_vertices:
            self.add_edge(Edge(d_vertex, sink, 2))

        # Add edges from p_vertices to c_vertices based on preferences
        for i, prefs in enumerate(preferences):
            p_vertex = p_vertices[i]
            for pref in prefs:
                c_vertex = c_vertices[pref]
                self.add_edge(Edge(p_vertex, c_vertex, 1))

        # Add edges from c_vertices to sink
        for c_vertex in c_vertices:
            self.add_edge(Edge(c_vertex, sink, 3))

class ResidualNetwork(NetworkFlow):
    def __init__(self, network):
        super().__init__()
        self.vertices = network.vertices
        self.edges = [Edge(edge.start_vertex, edge.end_vertex, edge.capacity, edge.flow) for edge in network.edges]

    def has_AugmentingPath(self, source, sink):
        queue = [source]
        source.visited = True

        while queue:
            vertex = queue.pop(0)
            for edge in self.edges:
                residual_capacity = edge.capacity - edge.flow
                if edge.start_vertex == vertex and not edge.end_vertex.visited and residual_capacity > 0:
                    edge.end_vertex.parent = edge  # Use the parent attribute of Vertex
                    if edge.end_vertex == sink:
                        self._reset_visited()
                        return True
                    queue.append(edge.end_vertex)
                    edge.end_vertex.visited = True
        self._reset_visited()
        return False

    def get_AugmentingPath(self, source, sink):
        path = []
        while sink != source:
            edge = sink.parent  # Use the parent attribute of Vertex
            path.insert(0, edge)
            sink = edge.start_vertex
        return path

    def _reset_visited(self):
        for vertex in self.vertices:
            vertex.visited = False
            #vertex.parent = None

    def augment_flow(self, path):
        # This method should update the flow in the residual network based on the augmenting path
        min_residual_capacity = min(edge.capacity - edge.flow for edge in path)
        for edge in path:
            edge.flow += min_residual_capacity

    def ford_fulkerson(self):
        flow=0
        while self.has_AugmentingPath(self.vertices[0], self.vertices[-1]):
            path= self.get_AugmentingPath(self.vertices[0], self.vertices[-1])
            min_residual_capacity = min(edge.capacity - edge.flow for edge in path)
            flow += min_residual_capacity
            self.augment_flow(path)
        return flow

    def get_connected_vertices(self):
        connected_vertices = []
        d_vertices = [vertex for vertex in self.vertices if vertex.name.startswith('d')]
        c_vertices = [vertex for vertex in self.vertices if vertex.name.startswith('c')]

        for d_vertex, c_vertex in zip(d_vertices, c_vertices):
            p_vertices_d = [edge.start_vertex.name for edge in self.edges if edge.end_vertex == d_vertex and edge.flow > 0]
            p_vertices_c = [edge.start_vertex.name for edge in self.edges if edge.end_vertex == c_vertex and edge.flow > 0]
            connected_vertices.append([p_vertices_d, p_vertices_c])
        connected_vertices= [sum(sublist, []) for sublist in connected_vertices]
        return connected_vertices

if __name__ == '__main__':
    preferences = [[0], [0, 1], [0], [1, 0], [1], [1]]
    licences = [4, 2, 0, 5]
    # Create vertices
    source1 = Vertex('source1')
    source2 = Vertex('source2')
    sink = Vertex('sink')
    p_vertices = [Vertex(f'p{i}') for i in range(6)]
    d_vertices = [Vertex(f'd{i}') for i in range(2)]
    c_vertices = [Vertex(f'c{i}') for i in range(2)]

    # Create network flow
    my_graph = NetworkFlow()
    for vertex in [source1, source2] + p_vertices + d_vertices + c_vertices + [sink]:
        my_graph.add_vertex(vertex)

    # Add edge from source1 to source2
    my_graph.add_edge(Edge(source1, source2, 6))

    # Add edges from source2 to p_vertices
    for p_vertex in p_vertices:
        my_graph.add_edge(Edge(source2, p_vertex, 1))

    # Add edges from p_vertices to d_vertices
    edges_from_p_to_d = {
        'p4': ['d1'],
        'p2': ['d0', 'd1'],
        'p0': ['d0'],
        'p5': ['d1'],
    }
    for p_name, d_names in edges_from_p_to_d.items():
        p_vertex = next(vertex for vertex in p_vertices if vertex.name == p_name)
        for d_name in d_names:
            d_vertex = next(vertex for vertex in d_vertices if vertex.name == d_name)
            my_graph.add_edge(Edge(p_vertex, d_vertex, 1))

    # Add edges from d_vertices to sink
    for d_vertex in d_vertices:
        my_graph.add_edge(Edge(d_vertex, sink, 2))

    # Add edges from p_vertices to c0
    for p_vertex in [p_vertices[i] for i in [0,1,2,3]]:
        my_graph.add_edge(Edge(p_vertex, c_vertices[0], 1))

    # Add edges from p_vertices to c1
    for p_vertex in [p_vertices[i] for i in [1,3,4,5]]:
        my_graph.add_edge(Edge(p_vertex, c_vertices[1], 1))

    # Add edges from c_vertices to sink
    for c_vertex in c_vertices:
        my_graph.add_edge(Edge(c_vertex, sink, 3))

    # Run Ford-Fulkerson algorithm
    residual=ResidualNetwork(my_graph)
    residual.ford_fulkerson()
    print(residual.get_connected_vertices())



