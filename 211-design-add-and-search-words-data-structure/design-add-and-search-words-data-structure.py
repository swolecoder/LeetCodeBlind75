class TrieNode:
    def __init__(self):
        self.children = {}
        self.endWord = False
    

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        root = self.root
        for ch in word:
            if ch not in root.children:
                root.children[ch] = TrieNode()
            root = root.children[ch]
        root.endWord = True

    def addWord(self, word: str) -> None:
        self.insert(word)

    def search(self, word: str) -> bool:
        stack = [(self.root, word)]
        
        while stack:
            node, curr_word = stack.pop()
            for i, w in enumerate(curr_word):
                if w == '.':
                    for child in node.children.values():
                        stack.append((child, curr_word[i + 1:]))
                    break
                elif w in node.children:
                    node = node.children[w]
                else:
                    break
            else:
                if node.endWord:
                    return True
        return False

      








        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)