class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0



class MapSum:

    def __init__(self):
        self.root = TrieNode()
        self.hashmap = {}

        
    def _insert(self, word,c):
        root = self.root
        delta = c
        if word not in self.hashmap:
            self.hashmap[word] = c
        else:
            v = self.hashmap[word]
            delta = c - v
            self.hashmap[word] = c


        for w in word:
            if w not in root.children:
                root.children[w] = TrieNode()
            root = root.children[w]
            root.count += delta
        #root.count = delta

    
    def _search(self, word):
        root = self.root
        c = 0

        for w in word:
            if w not in root.children:
                return 0
            root = root.children[w]
            # c += root.count  # Accumulate the count at each level
        return root.count

        

    def insert(self, key: str, val: int) -> None:
        self._insert(key,val)
        print(self.root)

        

    def sum(self, prefix: str) -> int:
        print(self.root)
        return self._search(prefix)
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)