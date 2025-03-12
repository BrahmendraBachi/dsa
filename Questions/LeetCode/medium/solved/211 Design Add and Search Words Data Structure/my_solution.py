class WordDictionary:

    def __init__(self):
        self.children = {}
        self.is_end = False

    def addWord(self, word: str) -> None:
        root = self
        for ch in word:
            order = ord(ch) - ord('a')
            if order not in root.children:
                root.children[order] = WordDictionary()
            root = root.children[order]
        root.is_end = True

    def search(self, word: str) -> bool:
        root = self
        if len(word) != 0:
            ch = word[0]
            order = ord(ch) - ord('a')
            if 0 <= order < 26:
                return order in root.children and root.children[order].search(word[1:])
            elif ch == ".":
                for child in root.children.values():
                    if child.search(word[1:]):
                        return True
                return False
            else:
                return False

        return self.is_end
