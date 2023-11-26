class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        root = self.root
        print(root)

        for w in word:
            if w not in root.children:
                root.children[w] = TrieNode()
            root = root.children[w]
        root.end = True
        

    def search(self, word: str) -> bool:
        root = self.root

        for w in word:
            if w not in root.children:
                return False
            root = root.children[w]
        
        return True if root.end == True else False
        

    def startsWith(self, prefix: str) -> bool:
        
        root = self.root

        for w in prefix:
            if w not in root.children:
                return False
            root = root.children[w]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)