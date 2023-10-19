
class Node:
    def __init__(self, data=(None, None, None), size=27):
        self.word = data[0]
        self.definition = data[1]
        self.frequency = data[2]
        self.node_frequency = 0
        self.link = [None] * size

class Trie:
    def __init__(self, Dictionary):
        self.root = Node()
        for words in Dictionary:
            self.insert(words[0], words)

    def insert(self, key, data):
        current = self.root
        current.node_frequency += 1
        if data is not None and current.frequency is not None:
            if data[2] > current.frequency:
                current.word, current.definition, current.frequency = data
        else:
            current.word, current.definition, current.frequency = data
        self.insert_aux(current, key, 0, data)

    def insert_aux(self, current, key, counter, data=None):
        if counter == len(key):
            current.link[0] = Node(data)
            current = current.link[0]
        else:
            char = key[counter]
            index = ord(char) - ord('a') + 1
            if current.link[index] is not None:
                current = current.link[index]
            else:
                current.link[index] = Node()
                current = current.link[index]
            current.node_frequency += 1
            if data is not None and current.frequency is not None:
                if data[2] > current.frequency:
                    current.word, current.definition, current.frequency = data
            else:
                current.word, current.definition, current.frequency = data
            self.insert_aux(current, key, counter+1, data)

    def prefix_search(self, key):
        current = self.root
        return self.prefix_search_aux(current, key)

    def prefix_search_aux(self, current, key):
        if len(key) == 0:
            return [current.word, current.definition, current.node_frequency]
        else:
            index = ord(key[0])-97+1
            if current.link[index] is not None:
                current = current.link[index]
            else:
                return [None, None, 0]
            return self.prefix_search_aux(current, key[1:])

if __name__ == "__main__":
