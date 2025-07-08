
class Trie:

    def __init__(self, val=""):
        self.val = val
        self.children = [None] * 26
        self.is_end = False

    def insert_word(self, word):
        node = self
        for ch in word:
            order = ord(ch) - ord('a')
            if not node.children[order]:
                node.children[order] = Trie(ch)
            node = node.children[order]
        node.is_end = True

    def search_word(self, word):
        node = self
        for ch in word:
            order = ord(ch) - ord('a')
            if not self.children[order]:
                return False
            node = node.children[order]
        return node.is_end


def main():
    trie = Trie("")

    trie.insert_word("bachi")
    print(trie.search_word("bachi"))
    print(trie.search_word("haci"))


if __name__ == "__main__":
    main()
