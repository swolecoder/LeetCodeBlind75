class Solution:
    def knightDialer(self, n: int) -> int:
        mapping = {
            0: [6, 4],
            1: [6, 8],
            2: [9, 7],
            3: [4, 8],
            4: [0, 9, 3],
            5: [],
            6: [0, 7, 1],
            7: [6, 2],
            8: [3, 1],
            9: [4, 2]
        }
        mod = 10**9 + 7  # Corrected to use integer arithmetic

        cache = {}

        def helper(remaining, currentDigit):
            key = (remaining, currentDigit)
            if key in cache:
                return cache[key]
            if remaining == 0:
                return 1
            ans = 0

            for digit in mapping[currentDigit]:
                ans += helper(remaining - 1, digit)  # Sum first, then apply modulo
            ans %= mod  # Apply modulo here after summing all paths
            cache[key] = ans
            return ans

        res = 0

        for i in range(10):
            res += helper(n - 1, i)
        
        res %= mod  # Apply modulo to the final result
        return int(res)
