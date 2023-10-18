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
    bipartite_network = FlowNetwork()

    # Adding vertices
    bipartite_network.addVertex("source", source=True)
    bipartite_network.addVertex("sink", sink=True)
    bipartite_network.addVertex("1")
    bipartite_network.addVertex("2")
    bipartite_network.addVertex("3")
    bipartite_network.addVertex("4")
    bipartite_network.addVertex("6")
    bipartite_network.addVertex("7")

    # Adding edges
    bipartite_network.addEdge("source", "1", 1)
    bipartite_network.addEdge("source", "2", 1)
    bipartite_network.addEdge("source", "3", 1)
    bipartite_network.addEdge("source", "4", 1)

    bipartite_network.addEdge("1", "7", 1)
    bipartite_network.addEdge("2", "6", 1)
    bipartite_network.addEdge("2", "7", 1)
    bipartite_network.addEdge("3", "6", 1)
    bipartite_network.addEdge("4", "6", 1)

    bipartite_network.addEdge("6", "sink", 2)
    bipartite_network.addEdge("7", "sink", 2)

    # Calculating max flow (which will represent the maximum matching)
    max_matching = bipartite_network.calculateMaxFlow()
    print(bipartite_network)


