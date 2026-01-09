class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False


class Solution:
    def create_trie(self, words):
        # === DO NOT MODIFY ===
        self.root = TrieNode()
        for word in words:
            self.insert(word)

    def insert(self, word):
        # === DO NOT MODIFY ===
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEndOfWord = True

    def search(self, word):
        """
        Search the trie for the given word.

        Returns True if the word exists in the trie, False otherwise
        """
        # === YOUR CODE HERE ===
        # start from the root node
        node = self.root

        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]

        return node.is_end

    def delete(self, word):
        """
        Deletes the given the word from the Trie.

        Returns None.
        """
        # === YOUR CODE HERE ===
        # an extra inner method: _delete
        def _delete(node, index):
            # base case: We have reached the end of the word
            if index == len(word):
                # Mark the node as not being the end of a word
                node.is_end = False
                # Return True if the node should be deleted
                return len(node.children) == 0

            char = word[index]
            child = node.children.get(char)

            if child is None:
                return False  # Word not found

            should_delete_child = _delete(child, index + 1)

            if should_delete_child:
                del node.children[char]

            # Return True if current node should be deleted
            return not node.is_end and len(node.children) == 0

        _delete(self.root, 0)

    def trie(self, initialWords, commands):
        # === DO NOT MODIFY ===
        self.create_trie(initialWords)

        output = []
        for command, word in commands:
            if command == "search":
                output.append(self.search(word))
            elif command == "delete":
                self.delete(word)
        return output