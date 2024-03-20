from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        c1 = Counter(t)
        c2 = {}

        have, need = 0, len(c1)  # need should be the number of unique characters in t

        res = [0, 0]
        resL = float("inf")
        left = 0

        for r in range(len(s)):
            ch = s[r]
            c2[ch] = c2.get(ch, 0) + 1

            if ch in c1 and c2[ch] == c1[ch]:
                have += 1

            while have == need:
                if (r - left + 1) < resL:  # Update the window if the current one is smaller
                    resL = r - left + 1
                    res = [left, r]

                c2[s[left]] -= 1
                if s[left] in c1 and c2[s[left]] < c1[s[left]]:
                    have -= 1

                left += 1

        l, r = res
        return s[l:r+1] if resL != float("inf") else ""  # Ensure to return the correct substring

                
















        