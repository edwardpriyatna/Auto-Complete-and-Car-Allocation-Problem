import math
import queue
import array

class Vertex:
    def __init__(self,id,name):
        self.id=id
        self.name=name
        self.edges=[] # a list that stores all the original edge and if in the residual network stores both the original and reverse
        self.pred=None #a predecessor edge

    def __str__(self):
        return f"id: {self.id} | name: {self.name} | predecessor: {self.pred}"

class Edge:
    def __init__(self,s,t,cap): #source, sink, capacity
        self.s=s
        self.t=t
        self.cap=cap
        self.flow=0
        self.rev=None

    def add_reverse_edge(self):
        reverse_edge = Edge(self.t, self.s, 0)
        reverse_edge.rev = self
        self.rev = reverse_edge
        self.s.edges.append(reverse_edge)  # add reverse edge to source vertex's edges list

    def __str__(self):
        return f"{self.s} -> {self.t} || Edge info: Capacity: {self.cap} | Flow: {self.flow}"

class Network:
    def __init__(self):
        self.vertices = []
        self.edges=[]

    def add_vertex(self,id, name):
        vertex = Vertex(id,name)
        self.vertices.append(vertex)
        return vertex

    def add_edge(self, s, t, cap):
        edge = Edge(s, t, cap)
        s.edges.append(edge)
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
        source = self.add_vertex(len(self.vertices),"source")
        sink = self.add_vertex(len(self.vertices),"sink")

        # Create p vertices and connect them to source
        p_vertices = [self.add_vertex(len(self.vertices),f"p{i}") for i in range(len(preferences))]
        for p_vertex in p_vertices:
            self.add_edge(source, p_vertex, 1)

        # Create d vertices
        num_d_vertices = math.ceil(len(preferences) / 5)
        d_vertices = [self.add_vertex(len(self.vertices),f"d{i}") for i in range(num_d_vertices)]

        # Connect p vertices with d vertices based on preferences and licenses
        for i, p_vertex in enumerate(p_vertices):
            if i in licenses:
                for pref in preferences[i]:
                    self.add_edge(p_vertex, d_vertices[pref], 1)

        # Create c vertices
        num_c_vertices = math.ceil(len(preferences) / 5)
        c_vertices = [self.add_vertex(len(self.vertices),f"c{i}") for i in range(num_c_vertices)]

        # Connect p vertices with c vertices based on preferences
        for i, p_vertex in enumerate(p_vertices):
            for pref in preferences[i]:
                self.add_edge(p_vertex, c_vertices[pref], 1)

        # Connect d vertices to sink with capacity 2
        for d_vertex in d_vertices:
            self.add_edge(d_vertex, sink, 2)

        # Create vertex e
        e_vertex = self.add_vertex(len(self.vertices),"e")

        # Connect c vertices to vertex e with capacity 3
        for c_vertex in c_vertices:
            self.add_edge(c_vertex, e_vertex, 3)

        # Connect vertex e to sink
        self.add_edge(e_vertex, sink, len(preferences)-math.ceil(len(preferences) / 5))

class ResidualNetwork:
    def __init__(self, network):
        self.vertices = network.vertices.copy()
        self.edges = network.edges.copy()
        self.create_residual_network()

    def create_residual_network(self):
        for edge in self.edges:
            edge.add_reverse_edge()  # call add_reverse_edge method for each edge

    def __str__(self):
        result = "Network:\n"
        for v in self.vertices:
            result += f"Vertex: {v}\n"
            for e in v.edges:
                result += f"  {e}\n"
        return result

    def bfs(self, source, sink):
        # Initialize the predecessor of each vertex
        for v in self.vertices:
            v.pred = None

        # Create a queue and add the source vertex to it
        vertex_queue = queue.Queue()
        vertex_queue.put(source)

        while not vertex_queue.empty() and self.vertices[sink.id].pred is None:
            # Get the next vertex from the queue
            current_vertex = vertex_queue.get()

            # Iterate over all edges coming out of 'current_vertex'
            for edge in self.vertices[current_vertex.id].edges:
                # If the end vertex of the edge has not been visited yet and the edge can carry more flow
                if self.vertices[edge.t.id].pred is None and edge.t != source and edge.cap > edge.flow:
                    # Set the predecessor of the end vertex to be 'edge'
                    self.vertices[edge.t.id].pred = edge

                    # Add the end vertex of the edge to the queue
                    vertex_queue.put(edge.t)

        # If we exited the loop without finding a path to the sink, then no augmenting path was found
        if self.vertices[sink.id].pred is None:
            return False

        # Otherwise, we found an augmenting path
        return True

    def edmonds_karp(self, source, sink):
        max_flow = 0
        while self.bfs(source, sink):
            path_flow = float('inf')
            s = sink
            while s != source:
                path_flow = min(path_flow, self.vertices[s.id].pred.cap - self.vertices[s.id].pred.flow)
                s = self.vertices[s.id].pred.s
            max_flow += path_flow
            v = sink
            while v != source:
                self.vertices[v.id].pred.flow += path_flow
                self.vertices[v.id].pred.rev.flow -= path_flow
                v = self.vertices[v.id].pred.s
        return max_flow

if __name__ == '__main__':
    preferences = [[1], [0, 1], [0], [0, 1], [0], [0]]
    licences = [0, 1, 2, 4]
    network=Network()
    network.make_network(preferences,licences)
    residual=ResidualNetwork(network)
    source=residual.vertices[0]
    sink=residual.vertices[1]
    residual.edmonds_karp(source,sink)
    print(residual)


