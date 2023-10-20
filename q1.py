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
        # Array of child nodes
        self.link = [None] * size

class Trie:
    def __init__(self, Dictionary):
        """
        Function description:
        Initializes a Trie with data from the given dictionary.

        :Input:
        Dictionary: A list of lists, where each for each inner index 0 is the word, index 1 is the definition, and
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

    def insert(self, key, data):
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
        sharing that key. It then calls the compare method to update the word information at each node with the
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
            # Increment the node_frequency to reflect the number of words sharing the key
            current.node_frequency += 1
            # Call the compare method to update word information
            self.compare(current, data, counter)
            # Recursively inserts the word
            self.insert_aux(current, key, counter + 1, data)

    def compare(self, current, data, counter=0):
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

    def prefix_search(self, prefix):
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

    def prefix_search_aux(self, current, prefix, counter):
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
            # Return [None, None, 0] if there is no matching node for the next character
            else:
                return [None, None, 0]
            # Continue the search recursively
            return self.prefix_search_aux(current, prefix, counter + 1)
