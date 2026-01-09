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

    def prefix(self, word):
        """
        Return a list of all words in the trie that start with the given prefix.
        """
        # === YOUR CODE HERE ===
        node = self.root
        for char in word:
            if char not in node.children:
                return []  # Prefix not found in trie
            node = node.children[char]

        # Now perform DFS to collect all words
        result = []

        def dfs(current_node, current_word):
            if current_node.is_end:
                result.append(current_word)

            for char, child_node in current_node.children.items():
                dfs(child_node, current_word + char)

        dfs(node, word)
        return result

    def trie(self, words, prefix):
        # === DO NOT MODIFY ===
        self.create_trie(words)
        return self.prefix(prefix)

