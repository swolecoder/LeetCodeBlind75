class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        half = (intLength +1) //2 
        start = 10 **(half-1)
        end = 10 ** half  -1

        print(half, start,end)

        ans = []

        for q in queries:
            half = start + q - 1 
            half_str = str(half)

            if half > end:
                ans.append(-1)
                continue

            if intLength %2 == 0:
                generate = int(half_str + half_str[::-1])
                print(generate)
                ans.append(generate)
            else:
                generate = int(half_str + half_str[-2::-1])
                print(generate)
                ans.append(generate)


        return ans