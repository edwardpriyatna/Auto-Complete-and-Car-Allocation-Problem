import math

class Vertex:
    def __init__(self, name):
        self.name = name
        self.edges = []  # list of edges connected to this vertex
        self.residual_edges = []  # list of residual edges connected to this vertex
        self.visited = False
        self.predecessor = None  # predecessor edge during BFS traversal

    def __str__(self):
        return self.name

class Edge:
    def __init__(self, origin, target, capacity):
        self.origin = origin
        self.target = target
        self.capacity = capacity
        self.flow = 0

    def __str__(self):
        return f"{self.origin} -> {self.target} | Capacity: {self.capacity} | Flow: {self.flow}"

class Network:
    def __init__(self):
        self.vertices = []
        self.edges = []

    def add_vertex(self, name):
        vertex = Vertex(name)
        self.vertices.append(vertex)
        return vertex

    def add_edge(self, source, target, capacity):
        edge = Edge(source, target, capacity)
        source.edges.append(edge)
        self.edges.append(edge)
        return edge

    def has_path(self, source, sink):
        # Reset visited state of all vertices
        for vertex in self.vertices:
            vertex.visited = False

        # Use BFS to find if a path exists
        queue = [source]
        while queue:
            vertex = queue.pop(0)
            vertex.visited = True
            if vertex == sink:
                return True
            for edge in vertex.edges:
                residual_capacity = edge.capacity - edge.flow
                if residual_capacity > 0 and not edge.target.visited:
                    edge.target.visited = True
                    queue.append(edge.target)
        return False

    def get_path(self, source, sink):
        # Reset visited state of all vertices and predecessors of all vertices
        for vertex in self.vertices:
            vertex.visited = False
            vertex.predecessor = None

        # Use BFS to find the shortest path
        queue = [source]
        while queue:
            vertex = queue.pop(0)
            vertex.visited = True
            if vertex == sink:
                break
            for edge in vertex.edges:
                residual_capacity = edge.capacity - edge.flow
                if residual_capacity > 0 and not edge.target.visited:
                    edge.target.visited = True
                    edge.target.predecessor = edge  # Set predecessor of the destination vertex
                    queue.append(edge.target)

        # Backtrack to find the path from source to sink using the predecessor attribute of each vertex
        path = []
        current_vertex = sink
        while current_vertex is not None and current_vertex.predecessor is not None:
            path.insert(0, current_vertex.predecessor)
            current_vertex = current_vertex.predecessor.origin

        return path if len(path) > 0 else None

    def __str__(self):
        result = "Network:\n"
        for v in self.vertices:
            result += f"Vertex: {v}\n"
            for e in v.edges:
                result += f"  {e}\n"
        return result

    def make_network(self, preferences, licenses):
        source = self.add_vertex('source')
        sink = self.add_vertex('sink')

        # Create p vertices and connect them to the source
        p_vertices = []
        for i in licenses:
            p_vertex = self.add_vertex(f'p{i}')
            self.add_edge(source, p_vertex, 1)
            p_vertices.append(p_vertex)

        # Create d vertices
        d_vertices = []
        for i in range(math.ceil(len(preferences) / 5)):
            d_vertex = self.add_vertex(f'd{i}')
            d_vertices.append(d_vertex)

        # Connect p vertices to d vertices based on preferences
        for p_vertex in p_vertices:
            i = int(p_vertex.name[1:])  # Get the index from the name of the p vertex
            for j in preferences[i]:
                self.add_edge(p_vertex, d_vertices[j], 1)

        # Connect d vertices to the sink
        for d_vertex in d_vertices:
            self.add_edge(d_vertex, sink, 2)

    def edmonds_karp(self, source, sink):
        # Initialize flow to 0 for all edges
        for edge in self.edges:
            edge.flow = 0

        while self.has_path(source, sink):
            # Find the path and calculate the minimum residual capacity
            path = self.get_path(source, sink)
            min_residual_capacity = min(edge.capacity - edge.flow for edge in path)

            # Augment the flow along the path
            for edge in path:
                edge.flow += min_residual_capacity

        # The maximum flow is the sum of flows into the sink
        return sum(edge.flow for edge in sink.edges)

if __name__ == '__main__':
    preferences = [[0], [1], [0, 1], [0, 1], [1, 0], [1], [1, 0], [0, 1], [1]]
    licences = [1, 4, 0, 5, 8]
    network=Network()
    network.make_network(preferences,licences)
    network.edmonds_karp(network.vertices[0],network.vertices[1])
    print(network)