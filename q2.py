import math

class Vertex:
    def __init__(self, name):
        self.name = name
        self.edges = []

    def __str__(self):
        return f"Vertex {self.name}"

class Edge:
    def __init__(self, start, end, capacity):
        self.start = start
        self.end = end
        self.capacity = capacity
        self.flow = 0
        self.reverseEdge = None

    def __str__(self):
        return f"Edge ({self.start} -> {self.end}) | Flow: {self.flow} | Capacity: {self.capacity}"

class FlowNetwork:
    def __init__(self):
        self.vertices = []

    def __str__(self):
        vertices_str = "\n".join(str(vertex) for vertex in self.vertices)
        edges_str = "\n".join(str(edge) for edge in self.getEdges())
        return f"Flow Network:\n\nVertices:\n{vertices_str}\n\nEdges:\n{edges_str}"

    def getVertex(self, name):
        for vertex in self.vertices:
            if name == vertex.name:
                return vertex

    def getEdges(self):
        allEdges = []
        for vertex in self.vertices:
            for edge in vertex.edges:
                allEdges.append(edge)
        return allEdges

    def addVertex(self, name):
        newVertex = Vertex(name)
        self.vertices.append(newVertex)

    def addEdge(self, start, end, capacity):
        newEdge = Edge(start, end, capacity)
        reverseEdge = Edge(end, start, 0)
        newEdge.reverseEdge = reverseEdge
        reverseEdge.reverseEdge = newEdge

        startVertex = self.getVertex(start)
        startVertex.edges.append(newEdge)

        endVertex = self.getVertex(end)
        endVertex.edges.append(reverseEdge)

    def getPath(self, start, end, path):
        if start == end:
            return path
        startVertex = self.getVertex(start)
        for edge in startVertex.edges:
            residualCapacity = edge.capacity - edge.flow
            if residualCapacity > 0 and not (edge, residualCapacity) in path:
                result = self.getPath(edge.end, end, path + [(edge, residualCapacity)])
                if result != None:
                    return result

    def calculateMaxFlow(self):
        source = self.vertices[0]
        sink = self.vertices[1]
        path = self.getPath(source.name, sink.name, [])
        while path != None:
            flow = min(edge[1] for edge in path)
            for edge, res in path:
                edge.flow += flow
                edge.reverseEdge.flow -= flow
            path = self.getPath(source.name, sink.name, [])
        sourceEdges = self.vertices[0].edges
        return sum(edge.flow for edge in sourceEdges)

    def create_network(self, preferences, licenses):
        # Create source and sink vertices
        self.addVertex("source")
        self.addVertex("sink")

        # Create vertices 0,1,...,len(preferences)-1 and connect them to source
        for i in range(len(preferences)):
            self.addVertex(str(i))
            self.addEdge("source", str(i), 1)

        # Create d vertices and connect them to sink
        num_d_vertices = math.ceil(len(preferences) / 5)
        for i in range(num_d_vertices):
            self.addVertex(f"d{i}")
            self.addEdge(f"d{i}", "sink", 2)

        # Connect number vertices to d vertices based on preferences and licenses
        for i, pref in enumerate(preferences):
            if i in licenses:
                for p in pref:
                    self.addEdge(str(i), f"d{p}", 1)

        # Create c vertices
        for i in range(num_d_vertices):
            self.addVertex(f"c{i}")

        # Connect number vertices to c vertices based on preferences
        for i, pref in enumerate(preferences):
            for p in pref:
                # Since the preferences for d and c vertices are the same, we can reuse the logic here
                self.addEdge(str(i), f"c{p}", 1)

        # Create vertex e and connect c vertices to e
        self.addVertex("e")
        for i in range(num_d_vertices):
            self.addEdge(f"c{i}", "e", 3)

        # Connect e to sink
        self.addEdge("e", "sink", len(preferences) - 2 * math.ceil(len(preferences) / 5))

    def getResults(self):
        results = []
        num_d_vertices = math.ceil(len(self.vertices) / 5)

        # For each d and c vertex pair, gather the connected number vertices
        for i in range(num_d_vertices):
            combined_list = []
            # Check each numbered vertex for connections to d or c vertices
            for v in self.vertices:
                if v.name.isnumeric():
                    for edge in v.edges:
                        if edge.flow > 0 and edge.end == f"d{i}":
                            combined_list.append(int(v.name))
                        elif edge.flow > 0 and edge.end == f"c{i}":
                            combined_list.append(int(v.name))
            if combined_list:  # Only add if there's a valid connection
                results.append(combined_list)
        return results

def allocate(preferences, licenses):
    if len(preferences)<2 or len(licenses) < math.ceil(len(preferences)/5):
        # each car need minimum 2 persons or there are not enough drivers for the amount of people
        return None
    network = FlowNetwork()
    network.create_network(preferences, licenses)
    max_flow=network.calculateMaxFlow()
    if max_flow < len(preferences): #this means not every person can be matched with a car that has 2 drivers
        return None
    return network.getResults()

if __name__ == '__main__':
    test_network = FlowNetwork()
    preferences = [[0], [1], [0, 1], [0, 1], [1, 0], [1], [1, 0], [0, 1], [1]]
    licenses = [1, 4, 0, 5, 8]
    test_network.create_bipartite_graph(preferences,licenses)
    test_network.calculateMaxFlow()
    print(test_network.getResults())

