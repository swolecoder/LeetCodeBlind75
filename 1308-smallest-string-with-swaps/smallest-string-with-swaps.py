from collections import defaultdict

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        parent = [i for i in range(len(s))]

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(y)] = find(x)
        
        # Perform union operations based on the pairs provided.
        for x, y in pairs:
            union(x, y)
        
        # Group indices by their root parent.
        groups = defaultdict(list)
        for i in range(len(s)):
            groups[find(i)].append(i)

        # Initialize the result array
        result = [''] * len(s)

        # Sort characters in each group and place them in the result array
        for group in groups.values():
            sorted_chars = sorted(s[i] for i in group)
            for i, char_index in enumerate(sorted(group)):
                result[char_index] = sorted_chars[i]
        
        # Convert the result array back to a string and return it
        return ''.join(result)
