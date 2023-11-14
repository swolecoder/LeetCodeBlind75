class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.map = TrieNode()
        

    def addWord(self, word: str) -> None:
        root = self.map

        for w in word:
            if w not in root.children:
                root.children[w] = TrieNode()
            root = root.children[w]
        root.end = True
        

    def search(self, word: str) -> bool:


        root = self.map

        def helper(word, root):
            for i,w in enumerate(word):
                if w not in root.children:
                    if w ==".":
                        for v in root.children.values():
                            if helper(word[i+1:], v):
                                return True
                            
                        return False
                    else:
                        return False
                else:
                    root = root.children[w]
            return root.end

        a= helper(word,root) 
        print(a)
        return a

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)