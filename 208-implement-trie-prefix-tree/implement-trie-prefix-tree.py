class Trie:

    def __init__(self):
        self.map = {}
        

    def insert(self, word: str) -> None:

        root = self.map

        for w in word:
            if w not in root:
                root[w] = {}
            root = root[w]
        root["end"] = True
        

    def search(self, word: str) -> bool:

        root  = self.map

        for w in word:
            if w not in root:
                return False
            root = root[w]
        print("Ashish",root)
        return True if "end" in root else False
        

    def startsWith(self, prefix: str) -> bool:

        root = self.map

        for w in prefix:
            if w  not in root:
                return False
            root = root[w]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)