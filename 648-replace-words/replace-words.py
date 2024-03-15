class TrieNode:
    def __init__(self):
        self.children = {}
        self.endWord = False

class Trie: 
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self,word):
        root = self.root

        for w in word:
            if w not in root.children:
                root.children[w] = TrieNode()
            root = root.children[w]
        root.endWord = True
    
    def search(self, find):
        root = self.root
        temp = ''

        for ch in find:
            if ch not in root.children:
                break
            temp += ch
            if root.children[ch].endWord:
                return temp
            root = root.children[ch]
        
        return ''

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for word in dictionary:
            trie.insert(word)
        data = sentence.split(' ')
        ans = []

        for i in range(len(data)):
            current = data[i]

            checker = trie.search(current)
            print('AShish',checker)
            if checker:
                print('Ranjan',checker)
                ans.append(checker)
            else:
                ans.append(current)
        
        print(ans)
        return ' '.join(ans)
        