import math

### DO NOT CHANGE THIS FUNCTION
def load_dictionary(filename):
    infile = open(filename)
    word, frequency = "", 0
    aList = []
    for line in infile:
        line.strip()
        if line[0:4] == "word":
            line = line.replace("word: ", "")
            line = line.strip()
            word = line
        elif line[0:4] == "freq":
            line = line.replace("frequency: ", "")
            frequency = int(line)
        elif line[0:4] == "defi":
            index = len(aList)
            line = line.replace("definition: ", "")
            definition = line.replace("\n", "")
            aList.append([word, definition, frequency])

    return aList

class Node:
    def __init__(self, data=(None, None, None), size=27):
        """
        Function description:
        Initializes a Node object to be used in Trie class.

        :Input:
        data: A tuple containing information about the word (word, definition, frequency).
        size: The size of the link array for child nodes.
        :Output, return or postcondition: Creates a Node object with the attributes being word, definition, frequency,
        node_frequency, and link.
        :Time complexity: O(1). Just initializing an object.
        :Aux space complexity: O(size). size is the number of elements initialized in self.link list
        """
        self.word = data[0]
        self.definition = data[1]
        self.frequency = data[2]
        self.node_frequency = 0
        # Create an array of child nodes
        self.link = [None] * size

class Trie:
    def __init__(self, Dictionary):
        """
        Function description:
        Initializes a Trie with data from the given dictionary.

        :Input:
        Dictionary: A list of lists, where each for each inner index 0 is the word, index 1 is the definition, and
        index 2 is the frquency of that word.
        :Output, return or postcondition: Initializes a Trie with a root node and populates it with data from the
        Dictionary.
        :Time complexity:
        O(T). T is the amount of characters in Dictionary.txt. Creates a Node for every character by inserting every
        word in Dictionary.txt.
        :Aux space complexity:
        O(T). T is the amount of characters in Dictionary.txt.Creates a Node for every character by inserting every
        word in Dictionary.txt.
        """
        self.root = Node()
        # Insert each word from the dictionary into the Trie
        for words in Dictionary:
            self.insert(words[0], words)

    def insert(self, key, data):
        """
        Function description:
        Inserts a word and its data into the Trie.

        Approach description (if main function):
        The insert method adds a word and its data to Trie object. Starting at root node, it adds the node_frequency
        by 1 and uses compare method in Trie class to store the data. Then, it calls insert_aux method and iterate
        through the characters of the word that is inserted.

        :Input:
        key: The word to insert.
        data: A list containing word information: word, definition, frequency.
        :Output, return or postcondition: Inserts the word and data into the Trie.
        :Time complexity: O(M*min(X, Y)), where M*min(X, Y) is the time complexity of insert_aux function.
        :Aux space complexity: O(M), where M is the aux space complexity of insert_aux function.
        """
        current = self.root
        # Increment the node frequency at the root node
        current.node_frequency += 1
        # Compare and store data at the current node
        self.compare(current, data)
        self.insert_aux(current, key, 0, data)

    def insert_aux(self, current, key, counter, data=None):
        """
        Function description:
        Auxiliary function for inserting a word and its data into the Trie.

        Approach description (if main function):
        The insert_aux method recursively adds a word and its data to Trie object. For each character in the word,
        it calculates the index for the corresponding child node based on the character's position in the alphabet.
        If a child node at the calculated index exists, it goes to that node. Else, it creates a new node at that index.
        The method adds the node_frequency at each node along the path, making sure it is the same the number of words
        sharing that prefix. Then it calls the compare method to update the word information at each node with the
        highest frequency and alphabetically smaller word. When the end of the word is reached, the word and data are
        stored in the 0th child node.

        :Input:
        current: The current node in the Trie.
        key: The word to insert.
        counter: The index of the word being processed.
        data: A list containing word information: word, definition, frequency.
        :Output, return or postcondition: Inserts the word and data into the Trie recursively.
        :Time complexity: O(M*min(X, Y)). M is the length of the key. The function is called M times recursively to
        insert each character in the key. Then compare is used that has O(min(X, Y)) time complexity.
        :Aux space complexity: O(M). M is the length of the key and the function creates a Node recursively for
        every character in the key if it not yet exists.
        """
        # Store the data in the first node when there is no more characters in the key
        if counter == len(key):
            current.link[0] = Node(data)
            current = current.link[0]
        else:
            # Get the character at the current position
            char = key[counter]
            # Calculate the index based on the character's position in the alphabet
            index = ord(char) - ord("a") + 1
            if current.link[index] is not None:
                # Move to the existing child node
                current = current.link[index]
            else:
                # Create a new child node if it does not exist
                current.link[index] = Node()
                # Move to the newly created child node
                current = current.link[index]
            # Increment the node_frequency to reflect the number of words sharing the prefix
            current.node_frequency += 1
            # Call the compare method to update word information
            self.compare(current, data, counter)
            # Recursively insert the word
            self.insert_aux(current, key, counter + 1, data)

    def compare(self, current, data, counter=0):
        """
        Function description:
        Compares the frequency of a newly inserted word with the frequency of the word already stored at a node and
        updates the node with the word in data if data and current.frequency is not None and the word in data has a
        higher frequency. If both have the same frequency, it will compare the words alphabetically to determine which
        is the smaller that will be stored. It does this by increasing the index each time until the characters are
        different.

        :Input:
        current: The current node in the Trie.
        data: A list containing word information: word, definition, frequency.
        :Output, return or postcondition: Updates the node with the word and data.
        :Time complexity: O(min(X, Y)). X is the number of characters in the current node's word. Y is the number of
        character in the data's word. The function compares the order of character in current node's word and
        data's word min(X, Y) times to determine if it will replace current node with data.
        :Aux space complexity: O(1)
        """
        if data is not None and current.frequency is not None:
            if data[2] > current.frequency:
                # Replace current node's data with the data if data's frequency is higher
                current.word, current.definition, current.frequency = data
            elif data[2] == current.frequency:
                # Compare the order of characters while the strings have characters and the characters are the same
                while counter < len(data[0]) and counter < len(current.word) and data[0][counter] == current.word[
                    counter]:
                    counter += 1
                if counter < len(data[0]) and counter < len(current.word) and data[0][counter] < current.word[counter]:
                    # Replace current with data if data is alphabetically smaller
                    current.word, current.definition, current.frequency = data
        else:
            # Set the current node's data to the data if data or current.frequency is None
            current.word, current.definition, current.frequency = data

    def prefix_search(self, key):
        """
        Function description:
        Performs a prefix search in the Trie.

        Approach description (if main function):
        This method searches a word and its associated data by its prefix in the Trie data structure.
        Starting at root node, it calls prefix_search_aux to perform to search recursively.

        :Input:
        key: The prefix to search for.
        :Output, return or postcondition: Returns a list containing word, definition, and node_frequency for the
        matching prefix.
        :Time complexity: O(M), where M is the time complexity of prefix_search_aux method.
        :Aux space complexity: O(1)
        """
        current = self.root
        return self.prefix_search_aux(current, key, 0)

    def prefix_search_aux(self, current, key, counter):
        """
        Function description:
        Auxiliary function for performing a prefix search in the Trie.

        Approach description (if main function):
        This method performs a prefix search recursively within the Trie. For each character in the prefix, it goes
        to the child node at the calculated index if it exists. If it doesn't exist, it returns [None, None, 0] meaning
        no matching word was found. The method continues the process, moving deeper into the Trie, until it reaches the
        end of the prefix. At the end of the prefix, it returns the information of the node: word, definition, and node
        frequency, which represents the words in the Trie that shares the prefix and has the highest frequency.

        :Input:
        current: The current node in the Trie.
        key: The prefix to search for.
        counter: The index of the prefix being processed.
        :Output, return or postcondition: Returns a list containing word, definition, and node_frequency for the
        matching prefix.
        :Time complexity: O(M), where M is the length of the prefix entered by the user and the function is called M
        times recursively to search each character of the prefix.
        :Aux space complexity: O(1)
        """
        # Return the information of the current node if the end of prefix is reached
        if counter == len(key):
            return [current.word, current.definition, current.node_frequency]
        else:
            char = key[counter]
            index = ord(char) - ord("a") + 1
            # Move to the next character's node if it exists
            if current.link[index] is not None:
                current = current.link[index]
            # Return [None, None, 0] if there is no matching node for the next character
            else:
                return [None, None, 0]
            # Continue the search recursively
            return self.prefix_search_aux(current, key, counter + 1)


class Vertex:
    def __init__(self, name):
        """
        Function description:
        Initializes a Vertex object to be used in FlowNetwork class.

        :Input:
        name: Name of the vertex.
        :Output, return or postcondition: Creates a vertex object with the attributes being name and edges.
        :Time complexity: O(1). Just initializing an object.
        :Aux space complexity: O(1). Just initializing a name and an empty list of edges.
        """
        self.name = name
        self.edges = [] #stores a list of all outgoing edges

    def __str__(self):
        return f"Vertex {self.name}"

class Edge:
    def __init__(self, origin, destination, capacity):
        """
        Function description:
        Initializes an Edge object to be used in FlowNetwork class.

        :Input:
        origin: The origin vertex.
        destination: The destination vertex.
        capacity: The capacity.
        :Output, return or postcondition: Creates a vertex object with the attributes being origin, destination,
        capacity, flow, and reverseEdge.
        :Time complexity: O(1). Just initializing an object.
        :Aux space complexity: O(1). Just initializing attributes.
        """
        self.origin = origin
        self.destination= destination
        self.capacity = capacity
        self.flow = 0
        self.reverseEdge = None

    def __str__(self):
        return f"Edge ({self.origin} -> {self.destination}) | Flow: {self.flow} | Capacity: {self.capacity}"

class FlowNetwork:
    def __init__(self):
        """
        Function description:
        Initializes a Flow Network object to be used in FlowNetwork class.

        :Input:
        Nothing
        :Output, return or postcondition: Creates a network object with the attributes being vertices which is a list
        of Vertex Objects in the FlowNetwork.
        :Time complexity: O(1). Just initializing an object.
        :Aux space complexity: O(1). Just initializing attributes.
        """
        self.vertices = []

    def __str__(self):
        vertices_str = "\n".join(str(vertex) for vertex in self.vertices)
        edges_str = "\n".join(str(edge) for edge in self.getEdges())
        return f"Flow Network:\n\nVertices:\n{vertices_str}\n\nEdges:\n{edges_str}"

    def getVertex(self, name):
        """
        Function description:
        Gets the vertex based on its name.

        :Input:
        name: Name of the vertex we want to search.
        :Output, return or postcondition: Returns the vertex we are looking for.
        :Time complexity: O(n). n being the length of self.vertices which is the same as the amount of persons.
        :Aux space complexity: O(1). It's in place.
        """
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
        """
        Function description:
        Adds a new vertex to self.vertices.

        :Input:
        name: Name which is the name of the vertex we want to add.
        :Output, return or postcondition: Adds a vertex to self.vertices.
        :Time complexity: O(1). We are creating and adding just 1 object at the end of the list.
        :Aux space complexity: O(1). Only creating 1 object.
        """
        newVertex = Vertex(name)
        self.vertices.append(newVertex)

    def addEdge(self, origin, destination, capacity):
        """
        Function description:
        Adds a new edge to the origin vertex and the corresponding reverse edge to the destination vertex.

        :Input:
        origin: The vertex the edge originates from.
        destination: The edge destination vertex.
        capacity: The capacity of the edge.
        :Output, return or postcondition: Adds an edge to the origin vertex.
        :Time complexity: O(1). We are creating and appending the edge to the originVertex.edges then we create the
        corresponding reverse edge and append them to destinationVertex.edges.
        :Aux space complexity: O(1). Only creating 2 objects.
        """
        newEdge = Edge(origin, destination, capacity)
        reverseEdge = Edge(destination, origin, 0)
        newEdge.reverseEdge = reverseEdge
        reverseEdge.reverseEdge = newEdge

        originVertex = self.getVertex(origin)
        originVertex.edges.append(newEdge)

        destinationVertex = self.getVertex(destination)
        destinationVertex.edges.append(reverseEdge)

    def getPath(self, origin, destination, path):
        """
        Function description:
        Recursively determines an augmenting path in the network using BFS.

        :Input:
        origin: The origin vertex name.
        destination: The destination vertex name.
        path: The current path (list of edges) being explored.

        :Output, return or postcondition:
        Returns an augmenting path from the source to the sink if one exists, else None.

        :Time complexity: O(V + E). In worst case, it would visit all the vertices and edges of the flow network.
        :Aux space complexity: O(V + E). It primarily comes from the recursion stack and the path list that stores the
        current path.
        """
        if origin == destination:
            return path
        originVertex = self.getVertex(origin)
        for edge in originVertex.edges:
            residualCapacity = edge.capacity - edge.flow
            if residualCapacity > 0 and not (edge, residualCapacity) in path:
                result = self.getPath(edge.destination, destination, path + [(edge, residualCapacity)])
                if result != None:
                    return result

    def calculateMaxFlow(self):
        """
        Function description:
        Calculates the maximum flow in the network using Ford-Fulkerson method.

        :Input: None
        :Output, return or postcondition:
        Returns the maximum flow value in the network.

        :Time complexity: O(VE^2). The Ford-Fulkerson algorithm's worst-case time complexity is O(VE^2)
        when using BFS to find augmenting paths.
        :Aux space complexity: O(V + E). Storage for vertices and edges.
        """
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
        """
        Function description:
        Constructs a bipartite flow network based on provided preferences and licenses.

        :Input:
        preferences: List of lists, where each inner list indicates preferences of a person.
        licenses: List of indices indicating which persons have licenses.

        :Output, return or postcondition:
        Creates a flow network that represents the problem.

        :Time complexity: O(n^2). n being the amount of persons. Most intensive operations involve nested loops over
        preferences.
        :Aux space complexity: O(n). The space complexity primarily grows with the number of preferences.
        """
        # Create source and sink vertices
        self.addVertex("source")
        self.addVertex("sink")

        # Create vertices 0,1,...,len(preferences)-1 to represent persons and connect them to source
        for i in range(len(preferences)):
            self.addVertex(str(i))
            self.addEdge("source", str(i), 1)

        # Create d vertices to represent drivers and connect them to sink
        num_d_vertices = math.ceil(len(preferences) / 5)
        for i in range(num_d_vertices):
            self.addVertex(f"d{i}")
            self.addEdge(f"d{i}", "sink", 2)

        # Connect number vertices to d vertices based on preferences and licenses
        for i, pref in enumerate(preferences):
            if i in licenses:
                for p in pref:
                    self.addEdge(str(i), f"d{p}", 1)

        # Create c to represent cars vertices
        for i in range(num_d_vertices):
            self.addVertex(f"c{i}")

        # Connect number vertices to c vertices based on preferences
        for i, pref in enumerate(preferences):
            for p in pref:
                self.addEdge(str(i), f"c{p}", 1)

        # Create vertex e as an intermediary vertex and connect c vertices to e
        self.addVertex("e")
        for i in range(num_d_vertices):
            self.addEdge(f"c{i}", "e", 3)

        # Connect e to sink and the edge's capacity is constraint for the amount of passengers
        self.addEdge("e", "sink", len(preferences) - 2 * math.ceil(len(preferences) / 5))

    def getResults(self):
        """
        Function description:
        Uses the flow network to determine the allocation of persons to cars.

        :Input: None
        :Output, return or postcondition:
        Returns a list of lists where each inner list represents a car's allocation of people.

        :Time complexity: O(n^2). n being the amount of persons. The method involves nested loops
        over person vertices and their edges.
        :Aux space complexity: O(n). Storage for results.
        """
        results = []
        num_d_vertices = math.ceil(len(self.vertices) / 5)

        # For each d and c vertex pair, gather the connected number vertices
        for i in range(num_d_vertices):
            combined_list = []
            # Check each numbered vertex for connections to d or c vertices
            for v in self.vertices:
                if v.name.isnumeric():
                    for edge in v.edges:
                        if edge.flow > 0 and edge.destination == f"d{i}":
                            combined_list.append(int(v.name))
                        elif edge.flow > 0 and edge.destination == f"c{i}":
                            combined_list.append(int(v.name))
            if combined_list:  # Only add if there's a valid connection
                results.append(combined_list)
        return results

def allocate(preferences, licenses):
    """
    Function description:
    Allocates persons to cars based on their preferences and available licenses.

    Approach description (if main function):
    I first create the network to represent this problem. Then I use calculateMaxFlow to give flow to the edges and
    return the max flow. Then using getResults if the person vertex is connected to either d or c vertices I put them
    into the corresponding lists.

    :Input:
    preferences: List of lists, where each inner list indicates preferences of a person.
    licenses: List of indices indicating which persons have licenses.

    :Output, return or postcondition:
    Returns a list of lists where each inner list represents a car's allocation of people.
    If allocation is not possible, it returns None.

    :Time complexity: O(n^3). n is the length of preferences. Mainly governed by calculateMaxFlow. Since time
    complexity of calculateMaxFlow is O(VE^2) becomes O(n*n^2) because v represents the number of vertices which in
    this case scales with number of persons and n^2 because the worst case will happen when everybody wants to go to
    every destination and everybody have license.
    :Aux space complexity: O(n). Space primarily grows with the number of preferences.
    """
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
    # Dictionary = load_dictionary("Dictionary.txt")
    # myTrie = Trie(Dictionary)
    # print(myTrie.prefix_search(""))
    # print(myTrie.prefix_search("a"))
    # print(myTrie.prefix_search("an"))
    # print(myTrie.prefix_search("ana"))
    # print(myTrie.prefix_search("anac"))
    # print(myTrie.prefix_search("anace"))
    preferences = [[0], [1], [0,1], [0, 1], [1, 0], [1], [1, 0], [0, 1], [1]]
    licences = [1, 4, 0, 5, 8]
    print(allocate(preferences, licences))

