class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1:
            return s

        res = [ [] for r in range(numRows)]
        

        for r in range(numRows):
            incre = (numRows- 1) * 2

            for i in range(r, len(s), incre):
                res[r].append(s[i])
                if r != 0  and r != numRows -1 and ( i + incre - 2* r < len(s) ):
                    res[r].append(s[i + incre - 2* r ])

        
        print(res)

        ans = ""
        for r in range(len(res)):
            ans += ''.join(res[r])
        
        return ans

        