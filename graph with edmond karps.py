class Vertex:
    def __init__(self, name, source=False, sink=False):
        self.name = name
        self.source = source
        self.sink = sink
        self.edges = []  # each vertex now has its own edges list

    def __str__(self):
        vertex_type = ""
        if self.source:
            vertex_type = "(Source)"
        elif self.sink:
            vertex_type = "(Sink)"
        return f"Vertex {self.name} {vertex_type}"

class Edge:
    def __init__(self, start, end, capacity):
        self.start = start
        self.end = end
        self.capacity = capacity
        self.flow = 0
        self.returnEdge = None

    def __str__(self):
        return f"Edge ({self.start} -> {self.end}) | Flow: {self.flow} | Capacity: {self.capacity}"

class FlowNetwork:
    def __init__(self):
        self.vertices = []

    def __str__(self):
        vertices_str = "\n".join(str(vertex) for vertex in self.vertices)
        edges_str = "\n".join(str(edge) for edge in self.getEdges())
        return f"Flow Network:\n\nVertices:\n{vertices_str}\n\nEdges:\n{edges_str}"

    def getSource(self):
        for vertex in self.vertices:
            if vertex.source:
                return vertex
        return None

    def getSink(self):
        for vertex in self.vertices:
            if vertex.sink:
                return vertex
        return None

    def getVertex(self, name):
        for vertex in self.vertices:
            if name == vertex.name:
                return vertex

    def vertexInNetwork(self, name):
        for vertex in self.vertices:
            if vertex.name == name:
                return True
        return False

    def getEdges(self):
        allEdges = []
        for vertex in self.vertices:
            for edge in vertex.edges:
                allEdges.append(edge)
        return allEdges

    def addVertex(self, name, source=False, sink=False):
        if source and sink:
            return "Vertex cannot be source and sink"
        if self.vertexInNetwork(name):
            return "Duplicate vertex"
        if source:
            if self.getSource() != None:
                return "Source already Exists"
        if sink:
            if self.getSink() != None:
                return "Sink already Exists"
        newVertex = Vertex(name, source, sink)
        self.vertices.append(newVertex)

    def addEdge(self, start, end, capacity):
        if start == end:
            return "Cannot have same start and end"
        if not self.vertexInNetwork(start):
            return "Start vertex has not been added yet"
        if not self.vertexInNetwork(end):
            return "End vertex has not been added yet"
        newEdge = Edge(start, end, capacity)
        returnEdge = Edge(end, start, 0)
        newEdge.returnEdge = returnEdge
        returnEdge.returnEdge = newEdge
        startVertex = self.getVertex(start)
        startVertex.edges.append(newEdge)
        endVertex = self.getVertex(end)
        endVertex.edges.append(returnEdge)

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
        source = self.getSource()
        sink = self.getSink()
        if source == None or sink == None:
            return "Network does not have source and sink"
        path = self.getPath(source.name, sink.name, [])
        while path != None:
            flow = min(edge[1] for edge in path)
            for edge, res in path:
                edge.flow += flow
                edge.returnEdge.flow -= flow
            path = self.getPath(source.name, sink.name, [])
        sourceEdges = self.getVertex(source.name).edges
        return sum(edge.flow for edge in sourceEdges)

if __name__ == '__main__':
    # Setting up the flow network for the described bipartite matching scenario
    bipartite_network_2 = FlowNetwork()

    # Adding vertices
    bipartite_network_2.addVertex("source", source=True)
    bipartite_network_2.addVertex("sink", sink=True)
    for i in range(6):
        bipartite_network_2.addVertex(f"p{i}")
    bipartite_network_2.addVertex("d0")
    bipartite_network_2.addVertex("d1")
    bipartite_network_2.addVertex("c0")
    bipartite_network_2.addVertex("c1")
    bipartite_network_2.addVertex("e")

    # Adding edges
    for i in range(6):
        bipartite_network_2.addEdge("source", f"p{i}", 1)

    bipartite_network_2.addEdge("p0", "d1", 1)
    bipartite_network_2.addEdge("p1", "d0", 1)
    bipartite_network_2.addEdge("p1", "d1", 1)
    bipartite_network_2.addEdge("p2", "d0", 1)
    bipartite_network_2.addEdge("p4", "d0", 1)

    bipartite_network_2.addEdge("d0", "sink", 2)
    bipartite_network_2.addEdge("d1", "sink", 2)

    bipartite_network_2.addEdge("p0", "c1", 1)
    bipartite_network_2.addEdge("p1", "c0", 1)
    bipartite_network_2.addEdge("p1", "c1", 1)
    bipartite_network_2.addEdge("p2", "c0", 1)
    bipartite_network_2.addEdge("p3", "c0", 1)
    bipartite_network_2.addEdge("p3", "c1", 1)
    bipartite_network_2.addEdge("p4", "c0", 1)
    bipartite_network_2.addEdge("p5", "c0", 1)

    # Continue adding the remaining edges for the described bipartite matching scenario

    bipartite_network_2.addEdge("c0", "e", 3)
    bipartite_network_2.addEdge("c1", "e", 3)

    bipartite_network_2.addEdge("e", "sink", 2)

    # Calculating max flow (which will represent the maximum matching)
    max_matching_2 = bipartite_network_2.calculateMaxFlow()
    print(max_matching_2)
    print(bipartite_network_2)


