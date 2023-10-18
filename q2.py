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

class ResidualEdge(Edge):
    def __init__(self, origin, target, capacity, original_edge=None):
        super().__init__(origin, target, capacity)
        self.original_edge = original_edge  # Reference to the original edge in the flow network
        self.forward_flow = 0
        self.backward_flow = 0

    def __str__(self):
        return f"{self.origin} -> {self.target} | Capacity: {self.capacity} " \
               f"| Forward Flow: {self.forward_flow}| Backward Flow: {self.backward_flow}"

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

        # Create vertex e
        e_vertex = self.add_vertex("e")

        # Connect c vertices to vertex e with capacity 3
        for c_vertex in c_vertices:
            self.add_edge(c_vertex, e_vertex, 3)

        # Connect vertex e to sink
        self.add_edge(e_vertex, sink, 3 * math.ceil(len(preferences) / 5))


class ResidualNetwork:
    def __init__(self, network):
        self.vertices = network.vertices.copy()
        self.edges = []
        self.residual_edges=[]
        self._create_residual_edges(network.edges)

    def _create_residual_edges(self, edges):
        for edge in edges:
            # Forward flow in the residual graph
            forward_flow = edge.capacity - edge.flow
            # Backward flow in the residual graph
            backward_flow = edge.capacity-forward_flow

            # Create the residual edge with both forward and backward flows and reference to the original edge
            residual_edge = ResidualEdge(edge.origin, edge.target, edge.capacity, original_edge=edge)
            residual_edge.forward_flow = forward_flow
            residual_edge.backward_flow = backward_flow

            # Add the residual edge to the respective vertices and to the global list
            edge.origin.residual_edges.append(residual_edge)
            self.residual_edges.append(residual_edge)

    def __str__(self):
        result = "Residual Network:\n"
        for v in self.vertices:
            result += f"Vertex: {v}\n"
            for e in v.residual_edges:
                result += f"  {e}\n"
        return result

    def _reset_visited_status(self):
        for vertex in self.vertices:
            vertex.visited = False

    def has_augmenting_path(self, origin, destination):
        # Reset visited status of all vertices
        self._reset_visited_status()

        # Initialize BFS list with the origin vertex
        bfs_list = [origin]
        origin.visited = True

        for current_vertex in bfs_list:
            if current_vertex == destination:
                return True

            for edge in current_vertex.residual_edges:
                # Check if the edge has capacity for more flow (i.e., backward_flow < capacity)
                if not edge.target.visited and edge.backward_flow < edge.capacity:
                    edge.target.visited = True
                    bfs_list.append(edge.target)
        return False

    def get_augmenting_path(self, origin, destination):
        # Reset visited status of all vertices
        self._reset_visited_status()

        # Initialize BFS list with the origin vertex
        bfs_list = [origin]
        origin.visited = True

        path_found = False
        for current_vertex in bfs_list:
            if current_vertex == destination:
                path_found = True
                break

            for edge in current_vertex.residual_edges:  # Assuming you store residual edges in 'edges' attribute
                # Check if the edge has capacity for more flow (i.e., backward_flow < capacity)
                if not edge.target.visited and edge.backward_flow < edge.capacity:
                    edge.target.visited = True
                    bfs_list.append(edge.target)
                    # Set the edge through which the vertex was reached as its predecessor
                    edge.target.predecessor = edge

        # If a path is found, reconstruct it using the predecessor attribute
        if path_found:
            path = []
            current_vertex = destination
            while current_vertex != origin:
                edge = current_vertex.predecessor
                path.append(edge)
                current_vertex = edge.origin  # Go to the vertex from which the current vertex was reached
            return path[::-1]  # Reverse the path to get it in the correct order from origin to destination
        return None  # Return None if no path is found

    def augment_path(self, path):
        # Identify the edge with the lowest forward_flow in the path
        min_forward_flow = min(edge.forward_flow for edge in path)

        # Update the backward_flow for each edge in the path
        for edge in path:
            # Add the minimum forward_flow to the backward_flow, ensuring it doesn't exceed the edge's capacity
            edge.backward_flow = min(edge.capacity, edge.backward_flow + min_forward_flow)

    def ford_fulkerson(self):
        while self.has_augmenting_path(self.vertices[0],self.vertices[1]):
            path=self.get_augmenting_path(self.vertices[0],self.vertices[1])
            self.augment_path(path)

if __name__ == '__main__':
    preferences = [[0], [1], [0, 1], [0, 1], [1, 0], [1], [1, 0], [0, 1], [1]]
    licences = [1, 4, 0, 5, 8]
    network=Network()
    network.make_network(preferences,licences)
    residual=ResidualNetwork(network)
    for vertex in residual.vertices:
        print(vertex)