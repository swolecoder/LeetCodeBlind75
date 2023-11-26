class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
        self.endWord  = ""
    def __str__(self):
        return f"TrieNode({self.children}, end={self.end})"

    def __repr__(self):
        return self.__str__()
class Solution:

    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, words):

        for word in words:
            root = self.root
            for w in word:
                if w not in root.children:
                    root.children[w] = TrieNode()
                root = root.children[w]
            root.end = True
            root.endWord = word

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        #insert the words as trie
        self.insert(words)

        R = len(board)
        C = len(board[0])
        path = set()
        res = []

        def dfs(r, c, node, word):
            if (r < 0 or c < 0 or r >= R or c >= C or 
                board[r][c] not in node.children or (r, c) in path):
                return False

            path.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]

            if node.end:
                res.append(word)  # Using a set to prevent duplicates
                node.end = False  # Remove 'end' marker to prevent finding the same word again

    # Explore adjacent cells
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)

            path.remove((r, c))

        
        for i in range(R):
            for j in range(C):
                dfs(i,j,self.root,"")
        return res
