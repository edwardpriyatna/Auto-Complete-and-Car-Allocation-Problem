import math
from queue import Queue
from typing import List, Tuple, Optional, Union

### DO NOT CHANGE THIS FUNCTION
def load_dictionary(filename):
    infile = open(filename)
    word, frequency = "", 0
    aList = []
    for line in infile:
        line.strip()
        if line[0:4] == "word":
            line = line.replace("word: ","")
            line = line.strip()
            word = line
        elif line[0:4] == "freq":
            line = line.replace("frequency: ","")
            frequency = int(line)
        elif line[0:4] == "defi":
            index = len(aList)
            line = line.replace("definition: ","")
            definition = line.replace("\n","")
            aList.append([word,definition,frequency])

    return aList

class Node:
    def __init__(self, data: Tuple[Optional[str], Optional[str], Optional[int]] = (None, None, None), size: int = 27):
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
        # Array of child nodes
        self.link = [None] * size

class Trie:
    def __init__(self, Dictionary):
        """
        Function description:
        Initializes a Trie with data from the given dictionary.

        :Input:
        Dictionary: A list of lists. Each inner index 0 is the word, index 1 is the definition, and
        index 2 is the frequency of that word.
        :Output, return or postcondition: Initializes a Trie with a root node and populates it with data from the
        Dictionary.
        :Time complexity:
        O(T). T is the amount of characters in Dictionary.txt. Creates a Node for every character by inserting every
        word in Dictionary.txt.
        :Aux space complexity:
        O(T). T is the amount of characters in Dictionary.txt. Creates a Node for every character by inserting every
        word in Dictionary.txt.
        """
        self.root = Node()
        # Inserts each word from dictionary into Trie
        for words in Dictionary:
            self.insert(words[0], words)

    def insert(self, key: str, data: Tuple[str, str, int]) -> None:
        """
        Function description:
        Inserts a word and its data into the Trie.

        Approach description (if main function):
        The insert method adds a word and its data to Trie object. Starting at root node, it adds the node_frequency
        by 1 and uses compare method in Trie class to store the data. It then calls insert_aux method and iterate
        through the characters of the word that is inserted.

        :Input:
        key: The word to insert.
        data: A list containing word information: word, definition, frequency.
        :Output, return or postcondition: Inserts the word and data into the Trie.
        :Time complexity: O(M*min(X, Y)), where M*min(X, Y) is the time complexity of insert_aux function.
        :Aux space complexity: O(M). M is the aux space complexity of insert_aux function.
        """
        current = self.root
        # Adds the node frequency at the root node
        current.node_frequency += 1
        # Compare and store data at the current node
        self.compare(current, data)
        self.insert_aux(current, key, 0, data)

    def insert_aux(self, current: Node, key: str, counter: int, data: Tuple[str, str, int] = None) -> None:
        """
        Function description:
        Auxiliary function for inserting a word and its data into the Trie.

        Approach description (if main function):
        The insert_aux method recursively adds a word and its data to Trie object. For each character in the word,
        it calculates the index for the corresponding child node based on the character's position in the alphabet.
        If a child node at the calculated index exists, it goes to that node. Else, it creates a new node at that
        index. The method adds the node_frequency at each node along the path, making sure it is the same the number
        of words sharing that key. It then calls the compare method to update the word information at each node with
        the highest frequency and alphabetically smaller word. When the end of the word is reached, the word and data
        are stored in the 0th child node.

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
            # Increment the node_frequency to reflect the number of words sharing the key
            current.node_frequency += 1
            # Call the compare method to update word information
            self.compare(current, data, counter)
            # Recursively inserts the word
            self.insert_aux(current, key, counter + 1, data)

    def compare(self, current: Node, data: Tuple[str, str, int], counter: int = 0) -> None:
        """
        Function description:
        Compares the frequency of a newly inserted word with the frequency of the word already stored at a node and
        updates the node with the word in data if data and current.frequency is not None and the word in data has a
        higher frequency. If both have the same frequency, it compares the words alphabetically to determine which
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

    def prefix_search(self, prefix: str) -> List[Union[str, int]]:
        """
        Function description:
        Returns the word with the highest frequency that has the given prefix, its definition, and the number of words
        that have the given prefix.

        Approach description (if main function):
        This method searches a word and its associated data by its prefix in the Trie data structure.
        Starting at root node, it calls prefix_search_aux to perform to search recursively.

        :Input:
        prefix: The prefix to search for.
        :Output, return or postcondition: Returns a list containing word, definition, and node_frequency for the
        matching prefix.
        :Time complexity: O(M). M is the time complexity of prefix_search_aux method.
        :Aux space complexity: O(1)
        """
        current = self.root
        return self.prefix_search_aux(current, prefix, 0)

    def prefix_search_aux(self, current: Node, prefix: str, counter: int) -> List[Union[str, int]]:
        """
        Function description:
        Auxiliary function for prefix_search.

        Approach description (if main function):
        This method performs a prefix search recursively within the Trie. For each character in the prefix, it goes
        to the child node at the calculated index if it exists. If it doesn't exist, it returns [None, None, 0] meaning
        no matching word was found. The method continues the process, moving deeper into the Trie, until it reaches the
        end of the prefix. At the end of the prefix, it returns the information of the node: word, definition, and node
        frequency, which represents the words in the Trie that shares the prefix and has the highest frequency.

        :Input:
        current: The current node in the Trie.
        prefix: The prefix to search for.
        counter: The index of the prefix being processed.
        :Output, return or postcondition: Returns a list containing word, definition, and node_frequency for the
        matching prefix.
        :Time complexity: O(M). M is the length of the prefix entered by the user and the function is called M
        times recursively to search each character of the prefix.
        :Aux space complexity: O(1)
        """
        # Return the information of the current node if the end of prefix is reached
        if counter == len(prefix):
            return [current.word, current.definition, current.node_frequency]
        else:
            char = prefix[counter]
            index = ord(char) - ord("a") + 1
            # Move to the next character's node if it exists
            if current.link[index] is not None:
                current = current.link[index]
                return self.prefix_search_aux(current, prefix, counter + 1)  # Continue the recursive search
            # Return [None, None, 0] if there is no matching node for the next character
            else:
                return [None, None, 0]


class Vertex:
    def __init__(self, name: str) -> None:
        """
        Function description:
        Initializes a Vertex object to be used in FlowNetwork class.

        :Input:
        name: Name of the vertex. A string.
        :Output, return or postcondition: Creates a vertex object with the attributes being name, edges, and visited.
        :Time complexity: O(1). Just initializing an object.
        :Aux space complexity: O(1). Just initializing a name and an empty list of edges.
        """
        self.name = name
        self.edges = [] #stores a list of all outgoing edges
        self.visited = False

class Edge:
    def __init__(self, origin: str, destination: str, capacity: int) -> None:
        """
        Function description:
        Initializes an Edge object to be used in FlowNetwork class.

        :Input:
        origin: The name of origin vertex. A string.
        destination: The name of destination vertex. A string.
        capacity: The capacity. An integer.
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

    def getVertex(self, name: str) -> Optional[Vertex]:
        """
        Function description:
        Gets the vertex based on its name.

        :Input:
        name: Name of the vertex we want to search. A string.
        :Output, return or postcondition: Returns the vertex we are looking for. A vertex object.
        :Time complexity: O(n). n being the length of self.vertices which is the same as the amount of persons.
        :Aux space complexity: O(1). It's in place.
        """
        for vertex in self.vertices:
            if name == vertex.name:
                return vertex

    def addVertex(self, name: str) -> None:
        """
        Function description:
        Adds a new vertex to self.vertices.

        :Input:
        name: Name which is the name of the vertex we want to add. A string.
        :Output, return or postcondition: Adds a vertex to self.vertices.
        :Time complexity: O(1). We are creating and adding just 1 object at the end of the list.
        :Aux space complexity: O(1). Only creating 1 object.
        """
        newVertex = Vertex(name)
        self.vertices.append(newVertex)

    def addEdge(self, origin: str, destination: str, capacity: int) -> None:
        """
        Function description:
        Adds a new edge to the origin vertex and the corresponding reverse edge to the destination vertex.

        :Input:
        origin: The name of the vertex the edge originates from. A string.
        destination: The name of the edge destination vertex. A string.
        capacity: The capacity of the edge. An integer.
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

    def getPath(self, origin: str, destination: str) -> Optional[List[Tuple[Edge, int]]]:
        """
        Function description:
        Determines an augmenting path in the network using BFS. It searches for a path from the origin to the
        destination that has available capacity.

        :Input:
        origin: The name of the origin vertex. A string
        destination: The name of the destination vertex. A string.

        :Output, return or postcondition:
        Returns an augmenting path from the source to the sink if one exists, else None. The path is represented as a
        list of tuples where each tuple contains an edge and its residual capacity.

        :Time complexity:
        O(V + E). V is the number of vertices and E is the number of edges. In the worst case, BFS would visit
        all the vertices and edges of the flow network.

        :Aux space complexity:
        O(V). Due to the BFS queue and the potential need to store paths for all vertices.
        """
        for vertex in self.vertices:
            vertex.visited = False

        # Using built-in Queue for BFS
        queue = Queue()
        queue.put((origin, []))
        while not queue.empty():
            (current_vertex_name, path) = queue.get()
            current_vertex = self.getVertex(current_vertex_name)

            if current_vertex_name == destination:
                return path

            if not current_vertex.visited:
                current_vertex.visited = True

                for edge in current_vertex.edges:
                    residual_capacity = edge.capacity - edge.flow
                    if residual_capacity > 0 and not (edge, residual_capacity) in path:
                        new_path = list(path)
                        new_path.append((edge, residual_capacity))
                        queue.put((edge.destination, new_path))  # Enqueue operation
        return None

    def calculateMaxFlow(self) -> int:
        """
        Function description:
        Calculates the maximum flow in the network and fills the edges with flow usingFord-Fulkerson with BFS.

        :Input: None

        :Output, return or postcondition:
        Returns the maximum flow value in the network. An integer.

        :Time complexity:
        O(F×(V+E)). F is the maximum flow value, V is the number of vertices, and E is the number of edges. Since
        the Ford-Fulkerson method runs as long as augmenting paths can be found and BFS in getPath is used to find
        paths, the complexity is derived from Ford-Fulkerson's iterations multiplied by the BFS time complexity.

        :Aux space complexity:
        O(V). Mainly governed by the BFS in getPath and storage needed to store the path.
        """
        source = self.vertices[0]
        sink = self.vertices[1]
        path = self.getPath(source.name, sink.name)
        while path != None:
            flow = min(edge[1] for edge in path)
            for edge, res in path:
                edge.flow += flow
                edge.reverseEdge.flow -= flow
            path = self.getPath(source.name, sink.name)
        sourceEdges = self.vertices[0].edges
        return sum(edge.flow for edge in sourceEdges)

    def create_network(self, preferences: List[List[int]], licenses: List[int]) -> None:
        """
        Function description:
        Constructs a bipartite flow network based on provided preferences and licenses.

        :Input:
        preferences: List of lists. Each inner list indicates preferences of a person.
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

    def getResults(self) -> List[List[int]]:
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

def allocate(preferences: List[List[int]], licenses: List[int]) -> Optional[List[List[int]]]:
    """
    Function description:
    Allocates persons to cars based on their preferences and available licenses using a flow network and the
    Ford-Fulkerson method.

    :Input:
    preferences (list): List of lists. Each inner list indicates preferences of a person.
    licenses (list): List of indices indicating which persons have licenses.

    :Output, return or postcondition:
    Returns a list of lists where each inner list represents a car's allocation of people. If allocation is not
    possible, it returns None.

    :Time complexity:
    O(n^3), where n is the length of preferences. The complexity is mainly governed by the calculateMaxFlow method.
    The Ford-Fulkerson method with BFS in getPath can lead to O(n*(n+n^2)) complexity. The max flow is the number of
    persons, V represents the number of vertices which scales with the number of persons, and n^2 is due to the worst
    case scenario where everybody wants to go to every destination and everybody has a license.

    :Aux space complexity:
    O(n), primarily determined by the space requirements of the flow network and the BFS traversal in `getPath`.
    """
    if len(preferences)<2 or len(licenses) < math.ceil(len(preferences)/5):
        # Each car need minimum 2 persons or there are not enough drivers for the amount of people
        return None
    network = FlowNetwork()
    network.create_network(preferences, licenses)
    max_flow=network.calculateMaxFlow()
    if max_flow < len(preferences): # Not every person can be matched with a car that has 2 drivers
        return None
    return network.getResults()


