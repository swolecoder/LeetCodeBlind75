class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        for i in range(len(strs[0])):
            for str in strs:
                if i == len(str) or strs[0][i] != str[i]:
                    return res
            
            res += strs[0][i]
        return res 