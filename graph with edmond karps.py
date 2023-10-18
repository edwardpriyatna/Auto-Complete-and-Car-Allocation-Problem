class Vertex:
    def __init__(self, name, source=False, sink=False):
        self.name = name
        self.source = source
        self.sink = sink
        self.edges = []  # each vertex now has its own edges list

class Edge:
    def __init__(self, start, end, capacity):
        self.start = start
        self.end = end
        self.capacity = capacity
        self.flow = 0
        self.returnEdge = None

class FlowNetwork:
    def __init__(self):
        self.vertices = []

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
    # Setting up the flow network for the described scenario
    network_suboptimal = FlowNetwork()
    network_suboptimal.addVertex("s", source=True)
    network_suboptimal.addVertex("t", sink=True)
    network_suboptimal.addVertex("a")
    network_suboptimal.addVertex("b")
    network_suboptimal.addEdge("s", "a", 10)
    network_suboptimal.addEdge("s", "b", 1)
    network_suboptimal.addEdge("a", "b", 1)
    network_suboptimal.addEdge("a", "t", 10)
    network_suboptimal.addEdge("b", "t", 10)

    # Calculate max flow
    max_flow_suboptimal = network_suboptimal.calculateMaxFlow()
    print(max_flow_suboptimal)

