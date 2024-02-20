from collections import defaultdict, deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        # if endWord not in wordList:
        #     wordList.append(endWord)
        nei = defaultdict(list)

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                nei[pattern].append(word)
        print(nei)

        q = deque([(beginWord, 1)])
        visited = set()

        while q:
            word, step = q.popleft()

            if word == endWord:
                return step 
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                for child in nei[pattern]:
                    if child not in visited:
                        visited.add(child)
                        q.append((child, step+1))
        return 0