class Node:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = Node()

    # Insert a word into the trie
    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = Node()
            current = current.children[char]
        current.is_end_of_word = True

    # Search for a word in the trie. True if exists
    def search(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_end_of_word

    # Word Starts with the given prefix
    def starts_with(self, prefix):
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True

    # Delete word from Trie
    def delete(self, word):
        def _delete(current, word, index):
            if index == len(word):
                if not current.is_end_of_word:
                    return False
                current.is_end_of_word = False
                return len(current.children) == 0

            char = word[index]
            if char not in current.children:
                return False

            can_delete_child = _delete(current.children[char], word, index + 1)

            if can_delete_child:
                del current.children[char]
                return len(current.children) == 0 and not current.is_end_of_word

            return False

        _delete(self.root, word, 0)


if __name__ == '__main__':
    trie = Trie()
    trie.insert("Apple")
    trie.insert("App")
    trie.insert("Banana")
    trie.insert("Bat")

    print(trie.search("Apple"))
    print(trie.search("App"))
    print(trie.search("Appl"))

    print()
    print(trie.starts_with("app"))
    print(trie.starts_with("App"))
    print(trie.starts_with("Bat"))
    print(trie.starts_with("Cat"))

    trie.delete("App")
    print()
    print(trie.search("App"))
    print(trie.search("Apple"))
