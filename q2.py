class Vertex:
    def __init__(self, name):
        self.name = name

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

class ResidualNetwork(NetworkFlow):
    def __init__(self, network):
        super().__init__()
        self.vertices = network.vertices
        self.edges = [Edge(edge.start_vertex, edge.end_vertex, edge.capacity, edge.flow) for edge in network.edges]
        self.parent = {vertex: None for vertex in self.vertices}

    def has_AugmentingPath(self, source, sink):
        # This is a simple BFS to check if there is a path from source to sink
        visited = {vertex: False for vertex in self.vertices}
        queue = [source]
        visited[source] = True

        while queue:
            vertex = queue.pop(0)
            for edge in self.edges:
                residual_capacity = edge.capacity - edge.flow
                if edge.start_vertex == vertex and not visited[edge.end_vertex] and residual_capacity > 0:
                    self.parent[edge.end_vertex] = edge
                    if edge.end_vertex == sink:
                        return True
                    queue.append(edge.end_vertex)
                    visited[edge.end_vertex] = True
        return False

    def get_AugmentingPath(self, source, sink):
        # This method should return the augmenting path as a list of edges
        path = []
        while sink != source:
            edge = self.parent[sink]
            path.append(edge)
            sink = edge.start_vertex
        path.reverse()
        return path

    def augment_flow(self, path):
        # This method should update the flow in the residual network based on the augmenting path
        min_residual_capacity = min(edge.capacity - edge.flow for edge in path)
        for edge in path:
            edge.flow += min_residual_capacity

def ford_fulkerson(my_graph):
    flow=0
    print('residual is:')
    residual_network=ResidualNetwork(my_graph)
    print(residual_network)
    while residual_network.has_AugmentingPath(residual_network.vertices[0], residual_network.vertices[-1]):
        path= residual_network.get_AugmentingPath(residual_network.vertices[0], residual_network.vertices[-1])
        min_residual_capacity = min(edge.capacity - edge.flow for edge in path)
        flow += min_residual_capacity
        residual_network.augment_flow(path)

    # Print the flow of each edge in the residual network
    print('the graph after ford fulkerson')
    print(residual_network)
    return flow

if __name__ == '__main__':
    # Create vertices
    source1 = Vertex('source1')
    source2 = Vertex('source2')
    sink = Vertex('sink')
    p_vertices = [Vertex(f'p{i}') for i in range(9)]
    d_vertices = [Vertex(f'd{i}') for i in range(2)]
    c_vertices = [Vertex(f'c{i}') for i in range(2)]

    # Create network flow
    my_graph = NetworkFlow()
    for vertex in [source1,source2] + p_vertices + d_vertices + c_vertices + [sink]:
        my_graph.add_vertex(vertex)

    # add edge from source 1 to source2
    my_graph.add_edge(Edge(source1,source2,9))

    # Add edges from source to p_vertices
    for p_vertex in p_vertices:
        my_graph.add_edge(Edge(source2, p_vertex, 1))

    # Add edges from p_vertices to d_vertices
    for p_vertex in [p_vertices[i] for i in [1, 4, 0, 5, 8]]:
        for d_vertex in d_vertices:
            my_graph.add_edge(Edge(p_vertex, d_vertex, 1))

    # Add edges from d_vertices to sink
    for d_vertex in d_vertices:
        my_graph.add_edge(Edge(d_vertex, sink, 2))

    # Add edges from p_vertices to c_vertices
    for p_vertex in [p_vertices[i] for i in [0, 2, 3, 6, 7]]:
        my_graph.add_edge(Edge(p_vertex, c_vertices[0], 1))
    for p_vertex in [p_vertices[i] for i in [1, 4, 5, 8]]:
        my_graph.add_edge(Edge(p_vertex, c_vertices[1], 1))

    # Add edges from c_vertices to sink
    for c_vertex in c_vertices:
        my_graph.add_edge(Edge(c_vertex, sink, 3))

    print('my graph is:')
    print(my_graph)
    ford_fulkerson(my_graph)


