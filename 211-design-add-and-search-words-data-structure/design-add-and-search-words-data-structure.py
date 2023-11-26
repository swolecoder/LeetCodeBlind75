#         Without Wildcards: If there are no wildcards in the word, the time complexity is O(m), where m is the length of the word. This is because, in the worst case, you need to traverse each character in the word exactly once.

# With Wildcards: The presence of wildcards complicates the time complexity. In the worst-case scenario, where the word consists entirely of wildcards (e.g., "...."), the time complexity becomes O(n^m), where n is the average branching factor of the nodes in the Trie, and m is the length of the word. This is because, for each wildcard character, the function potentially explores all child nodes at that level of the Trie.

# The branching factor n refers to the average number of children for each node in the Trie, which can vary depending on the dataset. In a typical English-language Trie, this could be up to 26 (for each letter of the alphabet), but it's often less in practice due to the uneven distribution of letter usage in words.

# Why O(n^m)?
# In the worst case, for each wildcard character, you have to explore all possible paths. If the Trie has a high branching factor, this can lead to a combinatorial explosion of paths to explore. The helper function is recursive, and with each wildcard, it makes up to n recursive calls (one for each child node), and this happens for each character in the word.

class WordDictionary:

    def __init__(self):
        self.map ={}
        

    def addWord(self, word: str) -> None:
        root = self.map

        for w in word:
            if w not in root:
                root[w] = {}
            root = root[w]
        root["end"] = True

        

    def search(self, word: str) -> bool:
        root = self.map
        

        def helper(word,root):
            for i,w  in enumerate(word):
                if w not in root:
                    if w == ".":
                        for v in root.values():
                            if isinstance(v, dict) and helper(word[i+1:], v):
                                return True
                        return False
                    
                    else:
                        return False
                else:
                    root = root[w]
            return True if "end" in root else False
        return helper(word, root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)