from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):  # If s1 is longer than s2, s1 can't be a permutation of any substring of s2.
            return False

        c1 = Counter(s1)
        c2 = Counter(s2[:len(s1)])

        for i in range(len(s2) - len(s1) + 1):
            if c1 == c2:
                return True
            if i + len(s1) < len(s2):  # Ensure we don't go out of bounds
                c2[s2[i + len(s1)]] += 1  # Add the new character
                c2[s2[i]] -= 1  # Remove the old character
                if c2[s2[i]] == 0:
                    del c2[s2[i]]  # Clean up zero counts

        return False


        