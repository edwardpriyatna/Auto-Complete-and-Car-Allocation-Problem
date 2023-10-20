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
        Initializes a Node object in a Trie.

        :Input:
        data: A tuple containing information about the word (word, definition, frequency).
        size: The size of the link array for child nodes.
        :Output, return or postcondition: Creates a Node with word, definition, frequency, node_frequency, and link
        attributes.
        :Time complexity: O(1)
        :Aux space complexity: O(size) where size is the number of elements initialized in self.link list
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
        Initializes a Trie with data from a given dictionary.

        :Input:
        Dictionary: A list of lists, where each inner list contains word information.
        :Output, return or postcondition: Initializes a Trie with a root node and populates it with data from the
        Dictionary.
        :Time complexity:
        O(T), where T is the total number of characters in Dictionary.txt and the function creates a Node for every
        character by performing insert method for every word in Dictionary.txt.
        :Aux space complexity:
        O(T), where T is the total number of characters in Dictionary.txt and the function creates a Node for every
        character by performing insert method for every word in Dictionary.txt.
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
        The insert method adds a word and its associated data to the Trie data structure. Starting at the root node, it
        increments node_frequency by 1 and performs compare method to store the data. Then, it calls its auxiliary
        method to iterate through the characters of the word to be inserted.

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
        The insert_aux method recursively adds a word and its associated data to the Trie data structure. For each
        character in the word, it calculates the index for the corresponding child node based on the character's
        position in the alphabet. If a child node at the calculated index exists, it advances to that node. Otherwise,
        it creates a new node at the index. The method increments the node_frequency count at each node along the path,
        ensuring it reflects the number of words sharing that prefix. It then calls the compare method to update the
        word information at each node with the highest frequency and alphabetically smaller word. When the end of the
        word is reached, the word and data are stored in the 0th child node.

        :Input:
        current: The current node in the Trie.
        key: The word to insert.
        counter: The index of the word being processed.
        data: A list containing word information: word, definition, frequency.
        :Output, return or postcondition: Inserts the word and data into the Trie recursively.
        :Time complexity: O(M*min(X, Y)), where M is the length of the key and the function is called M times
        recursively to insert each character in the key and in the process compare method is performed that has
        O(min(X, Y)) time complexity.
        :Aux space complexity: O(M), where M is the length of the key and the function creates a Node recursively for
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
        higher frequency. If both have the same frequency the function will compare the words alphabetically to
        determine which is smaller to store. It does this by increasing the index each time until the characters are
        different.

        :Input:
        current: The current node in the Trie.
        data: A list containing word information: word, definition, frequency.
        :Output, return or postcondition: Updates the node with the word and data.
        :Time complexity: O(min(X, Y)), where X is the number of characters in the current node's word and Y is the
        number of character in the data's word. The function compares the order of character in current node's word and
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
        The prefix_search method searches a word and its associated data by its prefix in the Trie data structure.
        Starting at the root node, it calls its auxiliary method to perform the search recursively.

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
        The prefix_search_aux method is responsible for performing a prefix search recursively within the Trie. For each
        character in the prefix, it advances to the child node at the calculated index if it exists. If the node doesn't
        exist, it returns [None, None, 0] to indicate that no matching word was found. The method continues the process,
        moving deeper into the Trie, until it reaches the end of the prefix. At the end of the prefix, it returns the
        information of the node: word, definition, and node frequency, which represents the words in the Trie that share
        the prefix and has the highest frequency.

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
