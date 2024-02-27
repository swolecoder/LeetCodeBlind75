from collections import deque, defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        map = defaultdict(list)

        for word in wordList:
            for j in range(len(word)):
                curr = word[:j] + "*"+ word[j+1:]
                map[curr].append(word)
        
        queue = deque([(beginWord,1)])
        seen = set()
        print(map)

        while queue:
            node,level = queue.popleft()

            if node == endWord:
                return level

            for j in range(len(node)):
                curr = node[:j]+"*"+ node[j+1:]
                for nei in map[curr]:
                    if nei not in seen:
                        seen.add(nei)
                        queue.append((nei, level+1))
        return 0

        