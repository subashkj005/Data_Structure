class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_End = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_End = True

    def search(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_End

    def delete_word(self, word):
        self.recur_delete(self.root, word, 0)

    def recur_delete(self, current, word, index):
        if index == len(word):
            # If the end-of-word node is found, mark it as not the end of a word anymore
            current.is_End = False
            # If the current node has no children, it can be deleted
            return len(current.children) == 0

        char = word[index]
        if char not in current.children:
            # If the character is not in the children of the current node, the word is not in the Trie
            return False

        # Recursively delete the next character in the word from the child node
        delete_boolean = self.recur_delete(current.children[char], word, index + 1)
        if delete_boolean:
            # If the child node was deleted, remove it from the current node's children
            del current.children[char]
            # If the current node has no children, it can be deleted
            return len(current.children) == 0

        # If the child node was not deleted, return False to propagate up the recursion stack
        return False

    def words_with_prefix_helper(self, node, prefix, words):
        if node.is_End:
            words.append(prefix)
        for char in node.children:
            self.words_with_prefix_helper(node.children[char], prefix + char, words)

    def words_with_prefix(self, prefix):
        current = self.root
        for char in prefix:
            if char not in current.children:
                return []
            current = current.children[char]
        words = []
        self.words_with_prefix_helper(current, prefix, words)
        return words

    def get_all_words(self):
        # Create an empty list to hold the words
        words = []
        # Traverse the Trie recursively, starting at the root node
        self._dfs(self.root, "", words)
        # Return the list of words
        print(words)
        return words

    def _dfs(self, node, prefix, words):
        # If the current node is an end-of-word node, add the current prefix to the list of words
        if node.is_End:
            words.append(prefix)
        # Recursively traverse the children of the current node
        for char, child_node in node.children.items():
            # Append the current character to the prefix and recursively traverse the child node
            self._dfs(child_node, prefix + char, words)





trie = Trie()
trie.insert("apple")
trie.insert("app")
trie.insert("application")
trie.insert("banana")
trie.insert("ball")
# print(trie.search("ball"))
# trie.delete_word("ball")
# print(trie.search("ball"))

# print("Words with prefix:-\n",trie.words_with_prefix("app"))

trie.get_all_words()
trie.delete_word("ball")
trie.get_all_words()




