from collections import defaultdict, deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        q = deque([(beginWord, 1)])
        check = set(wordList)
        seen = set()
        seen.add(beginWord)

        while q:
            word, length = q.popleft()
            if word == endWord:
                return length
            
            for i in range(len(word)):
                for ch in 'abcdefghijklmnopqrstuvwxyz':  # Fixed to include all lowercase letters
                    new_word = word[:i] + ch + word[i+1:]
                    if new_word in check and new_word not in seen:
                        q.append([new_word, length + 1])
                        seen.add(new_word)
        return 0

        