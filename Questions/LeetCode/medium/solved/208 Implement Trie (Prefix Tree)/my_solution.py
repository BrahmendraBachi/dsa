class Trie:

    def __init__(self, val: str = "0"):
        self.char = val
        self.children = []
        self.is_end = False

    def insert(self, word: str) -> None:
        if word == "":
            if self.char != 0:
                self.is_end = True
            return
        for child in self.children:
            if child.char == word[0]:
                return child.insert(word[1:])
        child = Trie(word[0])
        self.children.append(child)
        return child.insert(word[1:])

    def search(self, word: str) -> bool:
        if word == "":
            return self.is_end
        for child in self.children:
            if child.char == word[0]:
                return child.search(word[1:])

        return False

    def startsWith(self, prefix: str) -> bool:
        if prefix == "":
            return True
        for child in self.children:
            if child.char == prefix[0]:
                return child.startsWith(prefix[1:])
        return False

    def print_trie(self):
        root = self
        if not root:
            return
        for child in root.children:
            print(child.char, child.is_end)
            child.print_trie()

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)